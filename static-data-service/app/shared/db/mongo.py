from motor.motor_asyncio import AsyncIOMotorClient

url = "mongodb://localhost:27017/"
client = AsyncIOMotorClient(url)
db = client["semi-static-data"]