from uuid import uuid4,UUID
from pydantic import BaseModel, validator,validate_email,ValidationError
from typing import Optional

class AddressBase(BaseModel):
    id: Optional[int]
    email: str
    name: str
    address1: str
    city: str
    state: str
    country: str    
    zip: int
    phonenumber: int
    
    class Config:
        orm_mode = True
        
    # @validate_email('email')
    # def email_validation()
    