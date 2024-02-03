# FastApi simple CRUD app on student details with MongoDB as the database.

This is a simple fastApi CRUD app with MongoDB integration as the database that allows for performing CRUD (create,retrieve, update, and delete) on Student information.

## Table of Contents

- [Pre-requisites](#pre-requisites)
- [Getting Started](#Getting-started)
    - [Installation](#Installation)
    - [Database setup](#Database-setup)
- [Running the Api](#Starting-the-server)
- [Api Endpoints](#Api-endpoints)
    - [Create a student profile](#create-a-student-profile)
    - [Retrieve all student](#Retriev-all-student)
    - [Update a student profile](#Update-a-student-profile)
    - [Delete a student profile](#Delete-a-student)
- [Limitations and Assumptions](#Limitations-and-assumptions)


## Pre-requisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed.
- Pip package manager installed.
- A code editor (e.g., VSCode) for development.
- MongoDB install on your system.


## Getting Started

### Installation

1. Clone the repository:

        https://github.com/Pundit4Real/Fastapi-MongoDB-CRUD_app.git

2. Create a virtual environment (recommended):

        python -m venv ('environment name')

3. Activate the virtual environment:
   ```bash
   - On Windows:
   venv\Scripts\activate
   
   - On macOS and Linux:
   source venv/bin/activate

4. Install the required dependencies:

    `pip install -r requirements.txt`


### Database Setup

With MongoDB install on your system;
 
create a directory called __config.__
Inside the config directory, create a file called __database.py__ which will contain all the database connection codes.

Write this line of code in your database.py file to establish the connection with MongoDB server.

        from pymongo import MongoClient

        connection = MongoClient("mongodb://localhost:27017/student")


### Running the Api

*To start the server, run the following commands;*

        uvicorn your_app_name:app --reload 
        or
        python -m uvicorn your_app_name:app --reload

Replace your_app_name with the actual name of your FastAPI application file.

The endpoint will be available at 
__http://127.0.0.1:8000/docs__
