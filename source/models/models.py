from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from database import Base
from sqlalchemy import TIMESTAMP, Column, ForeignKey, String, Boolean, text
from uuid import uuid4

from sqlalchemy.dialects.postgresql import UUID

class Metadata(Base):
    __tablename__ = 'metadata'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4, unique=True, nullable=False)
    people = Column(String,nullable = True)
    places = Column(String , nullable=True)
    context = Column(String , nullable=True)

    @classmethod
    def from_request(cls, input):
        return cls(id=uuid4(),people=input.people, places=input.places,context=input.context)