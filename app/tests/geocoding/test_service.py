import pytest
from unittest.mock import AsyncMock, patch

from app.geocoding.service import search_place

@pytest.mark.asyncio
@patch("app.geocoding.service.query_city")
@patch("app.geocoding.service.get_geocode")
async def test_search_place_cache_hit(mock_get_geocode, mock_query_city):
    mock_query_city.return_value = {
        "results": [
            {"latitude": 48.85, "longitude": 2.35}
        ]
    }

    result = await search_place("Paris")

    mock_get_geocode.assert_not_called()
    assert result == {
        "latitude": 48.85,
        "longitude": 2.35
    }

@pytest.mark.asyncio
@patch("app.geocoding.service.query_city")
@patch("app.geocoding.service.get_geocode")
async def test_search_place_cache_miss(mock_get_geocode, mock_query_city):
    mock_query_city.return_value = None
    mock_get_geocode.return_value = {
        "results": [
            {"latitude": 40.71, "longitude": -74.0}
        ]
    }

    result = await search_place("New York")

    mock_get_geocode.assert_called_once()
    assert result["latitude"] == 40.71
