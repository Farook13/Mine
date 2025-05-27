from .mongo import db

files_col = db.files

async def insert_file(file_id, file_name, file_size, caption):
    await files_col.update_one(
        {"file_id": file_id},
        {"$set": {
            "file_name": file_name,
            "file_size": file_size,
            "caption": caption
        }},
        upsert=True
    )

async def get_file(file_id):
    return await files_col.find_one({"file_id": file_id})

async def search_files(query, limit=10):
    cursor = files_col.find({"file_name": {"$regex": query, "$options": "i"}}).limit(limit)
    return await cursor.to_list(length=limit)

async def total_files():
    return await files_col.count_documents({})
