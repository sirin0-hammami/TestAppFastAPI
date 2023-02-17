from typing import List

import sqlalchemy
from exceptions.custom_exception import NotFoundException
from source.services.metadata_services import Metadata_services
from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from fastapi import Depends
from source.models.metadata_model import Metadata
from source.schemas.metadata_schema import Metadata_schema

from source.db_helpers.database import my_db
from loguru import logger 


meta_router = APIRouter()
meta_services = Metadata_services()


@meta_router.get("/api/metadata" , response_model=List[Metadata])
async def index(db: Session = Depends(my_db.get_db)):
    return meta_services.get_all_metadata(db)

@meta_router.get("/api/metadata/{id}" , response_model=Metadata)
async def get_metadata_by_id(id : str , db: Session = Depends(my_db.get_db)):
    try :
      return meta_services.get_metadata(id, db)
    except NotFoundException : 
        raise HTTPException(status_code=404, detail="data not found") 
    
@meta_router.post("/api/metadata", response_model=Metadata)
async def add_metadata(metadata : Metadata_schema , db: Session = Depends(my_db.get_db)):
    return meta_services.post_metadata(metadata , db)

@meta_router.delete("/api/metadata/{id}" , response_model=Metadata)
async def remove_metadata(id : str, db: Session = Depends(my_db.get_db)):
    try :
      return meta_services.delete_metadata(id, db)
    except NotFoundException : 
        raise HTTPException(status_code=404, detail="data not found")
     
@meta_router.put("/api/metadata/{id}" , response_model=Metadata)
async def update_metadata(id : str , new_metadata : Metadata_schema, db: Session = Depends(my_db.get_db)):
    try :
      return meta_services.put_metadata(id, new_metadata ,db)
    except NotFoundException : 
        raise HTTPException(status_code=404, detail="data not found") 
