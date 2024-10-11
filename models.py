from datetime import datetime
from pydantic import BaseModel, EmailStr

# Define the Item model
class Item(BaseModel):
    # id: int  # Assuming you have an ID field for the item
    name: str
    email: EmailStr
    item_name: str
    quantity: int
    expiry_date: datetime
    insert_date: datetime = datetime.now()  # Automatically set to now when created

    class Config:
        orm_mode = True  # Enables compatibility with ORM models (like SQLAlchemy)

# Define the Clock-In Record model
class ClockInRecord(BaseModel):
    id: int  # Assuming you have an ID field for the clock-in record
    email: EmailStr  # Use EmailStr to validate the email format
    location: str  # Location as a string
    insert_datetime: datetime = datetime.now()  # Automatically set to now when created

    class Config:
        orm_mode = True  # Enables compatibility with ORM models (like SQLAlchemy)
