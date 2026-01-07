import httpx

# Private internal client variable
_http_client: httpx.AsyncClient | None = None

def get_client() -> httpx.AsyncClient:
    """Return the initialized client. Raises if not initialized."""
    if _http_client is None:
        raise RuntimeError("HTTP client not initialized")
    return _http_client

async def init_client():
    """Initialize the global client."""
    global _http_client
    _http_client = httpx.AsyncClient(timeout=10)

async def close_client():
    """Close the global client."""
    global _http_client
    if _http_client:
        await _http_client.aclose()
