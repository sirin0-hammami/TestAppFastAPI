from typing import List
from source.services.metadata_service import * 
from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends
from source.models.metadata_model import Metadata
from source.db_helpers.database import get_db

meta_router = APIRouter()

@meta_router.get("/" , response_model=List[Metadata])
async def index(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    return get_all_metadata(db, skip , limit)

@meta_router.get("/api/{id}" , response_model=Metadata)
async def get_metadata_by_id(id : str , db: Session = Depends(get_db)):
    return get_metadata(id, db)

@meta_router.post("/api", response_model=Metadata)
async def add_metadata(metadata : Data_schema , db: Session = Depends(get_db)):
    return post_metadata(metadata , db)

@meta_router.delete("/api/{id}" , response_model=Metadata)
async def remove_metadata(id : str, db: Session = Depends(get_db)):
    return delete_metadata(id , db)

@meta_router.put("/api/{id}" , response_model=Metadata)
async def update_metadata(id : str , new_metadata : Data_schema, db: Session = Depends(get_db)):
    return put_metadata(id, new_metadata , db )

 