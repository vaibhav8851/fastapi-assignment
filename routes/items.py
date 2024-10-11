from fastapi import APIRouter, HTTPException
from models import Item
from database import db
from bson import ObjectId
from datetime import datetime

router = APIRouter()

# POST /items
@router.post("/items")
def create_item(item: Item):
    item_dict = item.dict()
    item_dict['insert_date'] = datetime.utcnow().date()  # Automatically insert current date
    db.items.insert_one(item_dict)
    return {"message": "Item created successfully!"}

# GET /items/{id}
@router.get("/items/{id}")
def get_item(id: str):
    item = db.items.find_one({"_id": ObjectId(id)})
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    item['_id'] = str(item['_id'])  # Convert ObjectId to string for response
    return item

# GET /items/filter (for filters)
@router.get("/items/filter")
def filter_items(email: str = None, expiry_date: str = None, insert_date: str = None, quantity: int = None):
    query = {}
    if email:
        query['email'] = email
    if expiry_date:
        query['expiry_date'] = {"$gte": expiry_date}
    if insert_date:
        query['insert_date'] = {"$gte": insert_date}
    if quantity:
        query['quantity'] = {"$gte": quantity}
    
    items = list(db.items.find(query))
    for item in items:
        item['_id'] = str(item['_id'])  # Convert ObjectId to string for response
    return items

# MongoDB Aggregation: Count items by email
@router.get("/items/aggregate")
def aggregate_items_by_email():
    pipeline = [
        {"$group": {"_id": "$email", "count": {"$sum": 1}}}
    ]
    result = list(db.items.aggregate(pipeline))
    return result
