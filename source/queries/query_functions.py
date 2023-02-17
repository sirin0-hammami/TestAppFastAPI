import sqlalchemy
from source.models.metadata_model import Metadata
from sqlalchemy.orm import Session
from typing import List
from source.schemas.metadata_schema import Metadata_schema
from fastapi import HTTPException
from exceptions.custom_exception import NotFoundException
from sqlalchemy.exc import NoResultFound

class Metadata_queries : 
    def __init__(self):
        ...

    def get_query_all_data(self , db: Session, skip: int = 0, limit: int = 100) -> List[Metadata] :
        return db.query(Metadata).offset(skip).limit(limit).all()

    def get_query_by_id(self, id:int ,db: Session ) -> Metadata :
        try :
            data =  db.query(Metadata).filter(Metadata.id == id).one()
        except NoResultFound: 
            raise NotFoundException()
        return data 
    
    def post_query(self, metadata : Metadata_schema , db:Session ): 
        new_metadata = Metadata.from_request(metadata)
        db.add(new_metadata)
        db.commit()
        db.refresh(new_metadata)
        return new_metadata
    
    def delete_query(self,id:int,db:Session):
        """_summary_

        Parameters
        ----------
        id : int
            _description_
        db : Session
            _description_

        Returns
        -------
        _type_
            _description_

        Raises
        ------
        HTTPException
            _description_
        """
        data = self.get_query_by_id(id,db)
        db.delete(data)
        db.commit()
        return data
    
    def update_query(self, id:int, new_metadata : Metadata_schema , db:Session):
        data = self.get_query_by_id(id,db)
        new_data = new_metadata.dict(exclude_unset=True)
        for key, value in new_data.items():
            setattr(data, key, value)
        db.add(data)
        db.commit()
        db.refresh(data)
        return data






