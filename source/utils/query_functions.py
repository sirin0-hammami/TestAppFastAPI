from source.models.metadata_model import Metadata
from sqlalchemy.orm import Session
from fastapi import Depends
from source.db_helpers.database import get_db
from typing import List


def query_all_data(db: Session = Depends(get_db), skip: int = 0, limit: int = 100) -> List[Metadata] :
    return db.query(Metadata).offset(skip).limit(limit).all()

def query_by_id( id:int ,db: Session = Depends(get_db)) -> Metadata :
    return db.query(Metadata).filter(Metadata.id == id).one()




