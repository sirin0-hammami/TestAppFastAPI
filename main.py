from fastapi import FastAPI
import uvicorn
from source.api.metadata_routers import meta_router


app = FastAPI()

app.include_router(meta_router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)