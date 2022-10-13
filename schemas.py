from lib2to3.pgen2.token import OP
from uuid import uuid4,UUID
from pydantic import BaseModel,EmailStr
from typing import Optional

class AddressBase(BaseModel):
    email: EmailStr
    name: str
    address: str
    city: str
    state: str
    country: str    
    zip: int
    phonenumber: int
    latitude:str
    longitude:str
    
    class Config:
        orm_mode = True
        
class AddressBaseRequest(BaseModel):

    email: EmailStr
    name: str
    address: str
    city: str
    state: str
    country: str    
    zip: int
    phonenumber: int
    
    class Config:
        orm_mode = True
