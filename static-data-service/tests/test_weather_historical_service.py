import pytest
import httpx
from unittest.mock import AsyncMock, patch, MagicMock

from app.weather_historical.service import search_weather


# ── Month validation ──────────────────────────────────────────────────────────

@pytest.mark.asyncio
async def test_search_weather_invalid_month_zero_raises():
    with pytest.raises(ValueError, match="Month must be between 1 and 12"):
        await search_weather(51.5, -0.1, 0)


@pytest.mark.asyncio
async def test_search_weather_month_13_raises():
    with pytest.raises(ValueError, match="Month must be between 1 and 12"):
        await search_weather(51.5, -0.1, 13)


@pytest.mark.asyncio
async def test_search_weather_boundary_month_1_valid():
    fake_cached = MagicMock()
    with patch("app.weather_historical.service.query_weather", new_callable=AsyncMock, return_value=fake_cached):
        result = await search_weather(51.5, -0.1, 1)
    assert result is fake_cached


@pytest.mark.asyncio
async def test_search_weather_boundary_month_12_valid():
    fake_cached = MagicMock()
    with patch("app.weather_historical.service.query_weather", new_callable=AsyncMock, return_value=fake_cached):
        result = await search_weather(51.5, -0.1, 12)
    assert result is fake_cached


# ── Upstream API error propagation ───────────────────────────────────────────

@pytest.mark.asyncio
async def test_search_weather_upstream_error_propagates():
    mock_response = MagicMock()
    mock_response.status_code = 500

    with patch("app.weather_historical.service.query_weather", new_callable=AsyncMock, return_value=None):
        with patch("app.weather_historical.service.get_historical_weather", new_callable=AsyncMock) as mock_get:
            mock_get.side_effect = httpx.HTTPStatusError(
                "500", request=MagicMock(), response=mock_response
            )
            with pytest.raises(httpx.HTTPStatusError):
                await search_weather(51.5, -0.1, 6)


@pytest.mark.asyncio
async def test_search_weather_cache_hit_skips_upstream():
    """Cache hit must not call get_historical_weather."""
    fake_cached = MagicMock()
    with patch("app.weather_historical.service.query_weather", new_callable=AsyncMock, return_value=fake_cached):
        with patch("app.weather_historical.service.get_historical_weather", new_callable=AsyncMock) as mock_get:
            result = await search_weather(51.5, -0.1, 6)
    mock_get.assert_not_called()
    assert result is fake_cached
