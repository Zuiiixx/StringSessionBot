from motor.motor_asyncio import AsyncIOMotorClient
from env import DATABASE_URL

client = None
db = None

if DATABASE_URL != "":
    client = AsyncIOMotorClient(DATABASE_URL)
    db = client["stringsession"]  # change name as needed