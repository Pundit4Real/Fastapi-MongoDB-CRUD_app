from pydantic import BaseModel


class Blog(BaseModel):
    title: str
    description: str
    content: str
    author: str