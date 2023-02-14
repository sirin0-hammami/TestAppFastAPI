from pydantic import BaseSettings
from pydantic import BaseConfig

BaseConfig.arbitrary_types_allowed = True

class Settings(BaseSettings):
    DATABASE_PORT: int
    POSTGRES_PASSWORD: str
    POSTGRES_USER: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_HOSTNAME: str

    CLIENT_ORIGIN="http://localhost:8000"




settings = Settings()

