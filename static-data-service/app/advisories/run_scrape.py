from app.advisories.service import run_country_pipeline
import asyncio

if __name__ == "__main__":
    asyncio.run(run_country_pipeline())