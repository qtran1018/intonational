import sys
import os

# Ensure the static-data-service root is on sys.path so `app.*` imports resolve
# when this script is run directly (e.g., as a cron job)
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app.advisories.service import run_country_pipeline
import asyncio

if __name__ == "__main__":
    asyncio.run(run_country_pipeline())