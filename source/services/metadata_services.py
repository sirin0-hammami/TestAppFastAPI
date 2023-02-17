from source.models.metadata_model import Metadata
from sqlalchemy.orm import Session
from source.schemas.metadata_schema import Metadata_schema
from source.queries.query_functions import Metadata_queries
from typing import List

class Metadata_services:
    def __init__(self):
        self.query = Metadata_queries()

    def get_all_metadata(self , db:Session ) -> List[Metadata] :
        return self.query.get_query_all_data(db)

    def get_metadata(self,id : str , db: Session ) :
        return self.query.get_query_by_id(id , db)

    def post_metadata(self , metadata : Metadata_schema , db: Session) -> Metadata :
        return self.query.post_query(metadata , db)

    def delete_metadata(self , id : str, db: Session) -> Metadata :
        return self.query.delete_query(id, db)

    def put_metadata(self , id:int , new_metadata : Metadata_schema, db : Session) -> Metadata :
        return self.query.update_query(id,new_metadata,db)
