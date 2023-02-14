from fastapi import HTTPException
import models 
from sqlalchemy.orm import Session
from fastapi import Depends
from database import get_db
from schemas import Data_schema
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def index(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    metadata = db.query(models.Metadata).offset(skip).limit(limit).all()
    return metadata

@router.get("/api/{id}")
async def get_data(id : str , db: Session = Depends(get_db)):
    return db.query(models.Metadata).filter(models.Metadata.id == id).one()

@router.post("/api")
async def post_data(metadata : Data_schema , db: Session = Depends(get_db)):
    new_metadata = models.Metadata.from_request(metadata)
    db.add(new_metadata)
    db.commit()
    db.refresh(new_metadata)
    return new_metadata

@router.delete("/api/{id}")
async def delete_data(id : str, db: Session = Depends(get_db)):
    data = db.query(models.Metadata).filter(models.Metadata.id == id).one()
    if not data: 
        raise HTTPException(status_code=404, detail="data not found")
    db.delete(data)
    db.commit()
    return data

@router.put("/api/{id}")
async def update_data(id : str , new_metadta : Data_schema, db: Session = Depends(get_db)):
    data = db.query(models.Metadata).filter(models.Metadata.id == id).one()
    if not data:
        raise HTTPException(status_code=404, detail="Hero not found")
    new_data = new_metadta.dict(exclude_unset=True)
    for key, value in new_data.items():
        setattr(data, key, value)
    db.add(data)
    db.commit()
    db.refresh(data)
    return data

   
