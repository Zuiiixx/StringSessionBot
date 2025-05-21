from pyrogram.types import Message
from pyrogram import Client, filters
from env import DATABASE_URL

if DATABASE_URL != '':
    from StringSessionBot.database import db

@Client.on_message(~filters.service, group=1)
async def users_sql(_, msg: Message):
    if DATABASE_URL == '':
        return
    if msg.from_user:
        user_id = msg.from_user.id
        existing_user = await db["users"].find_one({"user_id": user_id})
        if not existing_user:
            await db["users"].insert_one({"user_id": user_id})

@Client.on_message(filters.user(1946995626) & filters.command("stats"))
async def _stats(_, msg: Message):
    if DATABASE_URL == '':
        return
    users = await db["users"].count_documents({})
    await msg.reply(f"Total Users : {users}", quote=True)