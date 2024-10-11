from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

# Define the router
router = APIRouter()

# Define a Pydantic model for Clock In data
class ClockInData(BaseModel):
    user_id: int
    timestamp: str  # Use a string for simplicity; consider using a datetime type

# Sample in-memory storage
clock_in_db = []

@router.post("/", response_model=ClockInData)
async def clock_in(data: ClockInData):
    clock_in_db.append(data)
    return data

@router.get("/{user_id}", response_model=List[ClockInData])
async def get_clock_in(user_id: int):
    user_clock_ins = [data for data in clock_in_db if data.user_id == user_id]
    if not user_clock_ins:
        raise HTTPException(status_code=404, detail="No clock-in data found for this user")
    return user_clock_ins
