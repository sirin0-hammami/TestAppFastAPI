from pydantic import BaseSettings
from pydantic import BaseConfig, Field
BaseConfig.arbitrary_types_allowed = True

class Settings(BaseSettings):
    DATABASE_PORT: int = Field("5432")
    POSTGRES_PASSWORD: str = Field("password123")
    POSTGRES_USER: str  = Field("postgres")
    POSTGRES_DB: str = Field("postgres")
    POSTGRES_HOST: str = Field("postgres")
    POSTGRES_HOSTNAME: str = Field("postgres")





settings = Settings()

