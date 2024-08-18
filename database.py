from pymongo import MongoClient
from datetime import datetime, timezone

mongo_client = MongoClient("localhost", 27017)

db = mongo_client['imperfecto_database'] 
collection = db['request_logs'] 


def log_user_request(user_id, request_type):
    log_entry = {
        "user_id": user_id,
        "request_type": request_type,
        "timestamp": datetime.now(timezone.utc)
    }

    result = collection.insert_one(log_entry)
    return result.inserted_id

#sample test
user_id = "pranav"
request_type = "user request"  
log_id = log_user_request(user_id, request_type)

print(f"Logged request with ID: {log_id}")