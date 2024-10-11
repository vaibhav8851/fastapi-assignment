from fastapi import APIRouter, HTTPException
from models import ClockInRecord
from database import db
from bson import ObjectId
from datetime import datetime

router = APIRouter()

# POST /clock-in
@router.post("/clock-in")
def create_clock_in(clock_in: ClockInRecord):
    clock_in_dict = clock_in.dict()
    clock_in_dict['insert_datetime'] = datetime.utcnow().isoformat()  # Automatically insert current date and time
    db.clock_in_records.insert_one(clock_in_dict)
    return {"message": "Clock-in record created successfully!"}

# GET /clock-in/{id}
@router.get("/clock-in/{id}")
def get_clock_in(id: str):
    record = db.clock_in_records.find_one({"_id": ObjectId(id)})
    if not record:
        raise HTTPException(status_code=404, detail="Clock-in record not found")
    record['_id'] = str(record['_id'])  # Convert ObjectId to string
    return record

# GET /clock-in/filter (for filters)
@router.get("/clock-in/filter")
def filter_clock_ins(email: str = None, location: str = None, insert_datetime: str = None):
    query = {}
    if email:
        query['email'] = email
    if location:
        query['location'] = location
    if insert_datetime:
        query['insert_datetime'] = {"$gte": insert_datetime}
    
    records = list(db.clock_in_records.find(query))
    for record in records:
        record['_id'] = str(record['_id'])  # Convert ObjectId to string for response
    return records

# DELETE /clock-in/{id}
@router.delete("/clock-in/{id}")
def delete_clock_in(id: str):
    result = db.clock_in_records.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Clock-in record not found")
    return {"message": "Clock-in record deleted successfully"}

# PUT /clock-in/{id}
@router.put("/clock-in/{id}")
def update_clock_in(id: str, clock_in: ClockInRecord):
    updated_data = clock_in.dict(exclude_unset=True)
    result = db.clock_in_records.update_one({"_id": ObjectId(id)}, {"$set": updated_data})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Clock-in record not found")
    return {"message": "Clock-in record updated successfully"}

