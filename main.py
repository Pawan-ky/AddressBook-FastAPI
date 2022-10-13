from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return "Hello, I am Pawan, building api using fast-api"


@app.get("/api/v1/address/getbyemail/",response_model=schemas.AddressBase)
def get_user_address(email:str, db: Session = Depends(get_db)):
    db_email = crud.get_address_by_email(db, email=email)
    if db_email is None:
        raise HTTPException(status_code=200, detail="Email not present")
    return db_email


@app.get("/api/v1/address/getall", response_model=list[schemas.AddressBase])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    address = crud.get_address(db, skip=skip, limit=limit)
    return address


@app.post("/api/v1/address/add/", response_model=schemas.AddressBase)
def add_address(address: schemas.AddressBaseRequest, db: Session = Depends(get_db)):
    db_email = crud.get_address_by_email(db, email=address.email)
    if db_email:
        raise HTTPException(status_code=400, detail="Email already present")
    return crud.add_address(db=db, address=address)


@app.put("/api/v1/address/update/",response_model=schemas.AddressBase)
def update_address(email:str,address: schemas.AddressBaseRequest,db: Session = Depends(get_db)):
    db_email = crud.get_address_by_email(db, email=email)
    if db_email is None:
        raise HTTPException(status_code=400, detail="Address with given email not found")
    return crud.update_address(db_email,db=db, address=address)

@app.delete("/api/v1/address/delete/")
def delete_address(email:str,db: Session = Depends(get_db)):
    db_isPresent = crud.get_address_by_email(db, email=email)
    if db_isPresent:
        db.delete(db_isPresent)
        db.commit()
        return "Address deleted Successfully"
    else:
        raise HTTPException(status_code=400, detail="Email not found")
