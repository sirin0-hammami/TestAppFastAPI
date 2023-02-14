from fastapi import FastAPI
from source.apis.metadata_routers import meta_router
import uvicorn
from source.db_helpers.database import Base,engine
from source.db_helpers.database import create_db

app = FastAPI()

create_db()

app.include_router(meta_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)