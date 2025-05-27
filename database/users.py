from .mongo import db
from datetime import datetime

users_col = db.users

async def add_user(user_id, name):
    user = await users_col.find_one({"user_id": user_id})
    if not user:
        await users_col.insert_one({
            "user_id": user_id,
            "name": name,
            "joined": datetime.utcnow()
        })

async def get_user(user_id):
    return await users_col.find_one({"user_id": user_id})

async def get_all_users():
    return users_col.find({}, {"_id": 0})

async def total_users():
    return await users_col.count_documents({})
