from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from configuration.config import settings
from source.models.metadata_model import Base

SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOSTNAME}:{settings.DATABASE_PORT}/{settings.POSTGRES_DB}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

def create_db() -> None: 
    Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> None:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
