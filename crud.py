from sqlalchemy.orm import Session

import models, schemas
from coordinates import get_coodinates


def get_address_by_id(db: Session, user_id: int):
    return db.query(models.Address).filter(models.Address.id == user_id).first()


def get_address_by_email(db: Session, email: str):
    return db.query(models.Address).filter(models.Address.email == email).first()


def get_address(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Address).offset(skip).limit(limit).all()


def add_address(db: Session, address: schemas.AddressBaseRequest):
    address_dict =  address.dict()
    address_for_coordinates = address_dict["address"]+","+address_dict["city"]
    # calling get_coordinates function to get corrdinates of address
    lat, lon = get_coodinates(address_for_coordinates)
    address_dict["latitude"] = lat
    address_dict["longitude"] = lon
    db_address = models.Address(**address_dict)
    db.add(db_address)
    db.commit()
    db.refresh(db_address)
    return db_address

def update_address(db_email,db: Session,address: schemas.AddressBase):
    dataToUpdate = address.dict(exclude_unset=True)
    address_for_coordinates = dataToUpdate["address"]+","+dataToUpdate["city"]
    # calling get_coordinates function to get corrdinates of address
    lat, lon = get_coodinates(address_for_coordinates)
    dataToUpdate["latitude"] = lat
    dataToUpdate["longitude"] = lon
    for key,value in dataToUpdate.items():
        setattr(db_email, key, value)
    db.add(db_email)
    db.commit()
    db.refresh(db_email)
    return db_email