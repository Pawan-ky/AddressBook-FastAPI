from decimal import Decimal
from enum import auto
from uuid import UUID
from sqlalchemy import Column, Integer, String


from database import Base


class Address(Base):
    __tablename__ = "address"

    email = Column(String,primary_key=True)
    name = Column(String)
    address = Column(String)
    city = Column(String)
    state = Column(String)
    country = Column(String)
    zip = Column(Integer)
    phonenumber = Column(Integer)
    latitude = Column(String)
    longitude = Column(String)
    
