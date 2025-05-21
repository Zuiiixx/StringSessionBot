from env import DATABASE_URL
from motor.motor_asyncio import AsyncIOMotorClient

if DATABASE_URL != "":
    client = AsyncIOMotorClient(DATABASE_URL)
    db = client["stringsession"]
    users_collection = db["users"]
else:
    client = None
    users_collection = None

class Users:
    def __init__(self, user_id, channels=None):
        self.user_id = user_id
        self.channels = channels or []

    async def save(self):
        if users_collection:
            await users_collection.update_one(
                {"user_id": self.user_id},
                {"$set": {"channels": self.channels}},
                upsert=True
            )

async def num_users():
    if users_collection:
        return await users_collection.count_documents({})
    return 0