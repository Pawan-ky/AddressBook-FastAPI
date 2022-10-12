from sqlalchemy.orm import Session

import models, schemas


def get_address_by_id(db: Session, user_id: int):
    return db.query(models.Address).filter(models.Address.id == user_id).first()


def get_address_by_email(db: Session, email: str):
    return db.query(models.Address).filter(models.Address.email == email).first()


def get_address(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Address).offset(skip).limit(limit).all()


def add_address(db: Session, address: schemas.AddressBase):
    db_address = models.Address(**address.dict())
    db.add(db_address)
    db.commit()
    db.refresh(db_address)
    return db_address

def update_address(db_email,db: Session,address: schemas.AddressBase):
    datToUpdate = address.dict(exclude_unset=True)
    
    for key,value in datToUpdate.items():
        setattr(db_email, key, value)
    db.add(db_email)
    db.commit()
    db.refresh(db_email)
    return db_email