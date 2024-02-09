from fastapi import APIRouter


endpoints = APIRouter()


@endpoints.get('/')
async def home():
    return {
        "string":"ok",
        "message":"My first api is running"
    }