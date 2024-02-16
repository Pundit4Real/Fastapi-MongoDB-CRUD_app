from fastapi import APIRouter
from config.config import blogsCollection
from models.models import Blog
from serializer.serializer import convertBlog,convertBlogs
from bson import ObjectId

endpoints = APIRouter()


@endpoints.post('/newblog')
async def create_blog(blog:Blog):
    blogsCollection.insert_one(dict(blog))
    return {
        "status": "ok",
        "message":"Data inserted"
    }

@endpoints.get("/allBlogs")
async def get_All_Blogs():
    blogs = blogsCollection.find()
    convertedBlogs = convertBlogs(blogs)
    return {
        "status": "ok",
        "data": convertedBlogs
    }

@endpoints.get("/blog/{id}")
def get_Blog(id:str):
    blog = blogsCollection.find_one({"_id":ObjectId(id)})
    convertedBlog= convertBlog(blog)
    return {
        "status":"ok",
        "data": convertedBlog
    }

@endpoints.patch("/update/{id}")
async def update_blog(id:str,blog:Blog):
    blogsCollection.find_one_and_update(
        {"_id":ObjectId(id)},
        {"$set":dict(blog)}
    )
    return {
        "status": "ok",
        "message": "Data have been updated"
    }

@endpoints.delete("/delete/{id}")
async def delete_blog(id:str):
    blogsCollection.find_one_and_delete({"_id":ObjectId(id)})
    return {
        "status":"ok",
        "message": "Blog have deleted successfully"
    }
