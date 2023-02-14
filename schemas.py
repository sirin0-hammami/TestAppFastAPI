from pydantic import BaseModel 

class Data_schema(BaseModel):
    people = ""
    places = ""
    context = "" 
    class Config:
        orm_mode = True