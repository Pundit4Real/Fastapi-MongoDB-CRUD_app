#import statement

from pydantic import BaseModel

class Student(BaseModel):
    Student_name: str
    student_email: str
    student_phone: str