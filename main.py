from fastapi import FastAPI
from dotenv import load_dotenv
from api.apiv1 import api_v1

load_dotenv()

app = FastAPI()

app.include_router(api_v1)


@app.get("/")
def hello():
    return {"message": "Hello World"}
