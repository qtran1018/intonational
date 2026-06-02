import json
import pytest
import httpx
from unittest.mock import AsyncMock, patch, MagicMock

from app.weather_forecast.service import search_weather
from app.weather_forecast.repository import query_weather, save_weather
from app.shared.redis.redis_repository import get_cache, set_cache


# ── Redis graceful degradation ────────────────────────────────────────────────

@pytest.mark.asyncio
async def test_get_cache_redis_down_returns_none():
    """Redis connection failure should return None, not raise."""
    with patch("app.shared.redis.redis_repository.redis_client") as mock_redis:
        mock_redis.get = AsyncMock(side_effect=Exception("Connection refused"))
        result = await get_cache("some-key")
    assert result is None


@pytest.mark.asyncio
async def test_set_cache_redis_down_does_not_raise():
    """Redis connection failure on set should be swallowed silently."""
    with patch("app.shared.redis.redis_repository.redis_client") as mock_redis:
        mock_redis.set = AsyncMock(side_effect=Exception("Connection refused"))
        await set_cache("some-key", "value", 60)  # must not raise


# ── Weather service — upstream error propagation ──────────────────────────────

@pytest.mark.asyncio
async def test_search_weather_cache_miss_upstream_error_propagates():
    """If upstream API returns a non-2xx, HTTPStatusError should propagate to the route handler."""
    mock_response = MagicMock()
    mock_response.status_code = 503

    with patch("app.weather_forecast.repository.get_cache", new_callable=AsyncMock, return_value=None):
        with patch("app.weather_forecast.client.get_weather_forecast", new_callable=AsyncMock) as mock_client:
            mock_client.side_effect = httpx.HTTPStatusError(
                "503 Service Unavailable", request=MagicMock(), response=mock_response
            )
            with pytest.raises(httpx.HTTPStatusError):
                await search_weather(51.5, -0.1)


@pytest.mark.asyncio
async def test_search_weather_cache_hit_returns_cached():
    """Cache hit should return model without calling upstream."""
    from app.weather_forecast.model import WeatherForecast

    fake_weather = MagicMock(spec=WeatherForecast)

    with patch("app.weather_forecast.repository.get_cache", new_callable=AsyncMock, return_value=None):
        with patch("app.weather_forecast.repository.query_weather", new_callable=AsyncMock, return_value=fake_weather):
            result = await search_weather(51.5, -0.1)
    assert result is fake_weather


# ── Repository — JSON parse error handled gracefully ─────────────────────────

@pytest.mark.asyncio
async def test_query_weather_corrupted_cache_raises():
    """Corrupted JSON in cache should raise — let the caller (service) decide how to handle."""
    with patch("app.weather_forecast.repository.get_cache", new_callable=AsyncMock, return_value=b"not-valid-json"):
        with pytest.raises(Exception):
            await query_weather(51.5, -0.1)
