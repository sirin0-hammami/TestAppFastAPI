from sqlalchemy import Column,String
from sqlalchemy import Column, String
from uuid import uuid4
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID

Base = declarative_base()

class Metadata(Base):
    __tablename__ = 'metadata'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4, unique=True, nullable=False)
    people = Column(String,nullable = True)
    places = Column(String , nullable=True)
    context = Column(String , nullable=True)

    @classmethod
    def from_request(cls, input):
        return cls(id=uuid4(),people=input.people, places=input.places,context=input.context)