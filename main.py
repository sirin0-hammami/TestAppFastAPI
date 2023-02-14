from fastapi import FastAPI
import models 
from database import engine
import uvicorn

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)