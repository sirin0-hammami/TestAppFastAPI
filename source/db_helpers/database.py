from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from configuration.config import settings
from source.models.metadata_model import Base

SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOSTNAME}:{settings.DATABASE_PORT}/{settings.POSTGRES_DB}"

engine = create_engine(
SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Database():
    def __init__(self):
        pass
    
    def create_db(self) -> None: 
        Base.metadata.create_all(bind=engine)

    def get_db(self) -> None:
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()


my_db = Database()
my_db.create_db()

