from fastapi import APIRouter
from models.student import Student
from config.database import connection


student_router = APIRouter()

@student_router.get('/hello')
async def hello_world():
    return "Hello world!"

@student_router.get('/students')
async def find_all_student():
    return connection.local.student.find()