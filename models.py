from enum import auto
from uuid import UUID
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Address(Base):
    __tablename__ = "address"

    id = Column(Integer,autoincrement=1)
    email = Column(String,primary_key=True)
    name = Column(String)
    address1 = Column(String)
    city = Column(String)
    state = Column(String)
    country = Column(String)
    zip = Column(Integer)
    phonenumber = Column(Integer)

    # items = relationship("Item", back_populates="owner")


# class Item(Base):
#     __tablename__ = "items"

#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, index=True)
#     description = Column(String, index=True)
#     owner_id = Column(Integer, ForeignKey("users.id"))

#     owner = relationship("User", back_populates="items")
