from pydantic import BaseModel 

class Metadata_schema(BaseModel):
    people = ""
    places = ""
    context = "" 
    class Config:
        orm_mode = True