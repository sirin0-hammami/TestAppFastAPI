from fastapi import HTTPException
from source.models.metadata_model import Metadata
from sqlalchemy.orm import Session
from fastapi import Depends
from source.db_helpers.database import get_db
from source.schemas.metadata_schemas import Data_schema
from source.utils.query_functions import query_all_data , query_by_id
from typing import List

def get_all_metadata(db: Session = Depends(get_db), skip: int = 0, limit: int = 100) -> List[Metadata] :
    return query_all_data(db, skip, limit )

def get_metadata(id : str , db: Session = Depends(get_db)) :
    return query_by_id(id , db)

def post_metadata(metadata : Data_schema , db: Session = Depends(get_db)) -> Metadata :
    new_metadata = Metadata.from_request(metadata)
    db.add(new_metadata)
    db.commit()
    db.refresh(new_metadata)
    return new_metadata

def delete_metadata(id : str, db: Session = Depends(get_db)) -> Metadata :
    data = query_by_id(id , db)
    if not data: 
        raise HTTPException(status_code=404, detail="data not found")
    db.delete(data)
    db.commit()
    return data

def put_metadata(id , new_metadata, db) -> Metadata :
    data = query_by_id(id , db)
    if not data:
        raise HTTPException(status_code=404, detail="data not found")
    new_data = new_metadata.dict(exclude_unset=True)
    for key, value in new_data.items():
        setattr(data, key, value)
    db.add(data)
    db.commit()
    db.refresh(data)
    return data

