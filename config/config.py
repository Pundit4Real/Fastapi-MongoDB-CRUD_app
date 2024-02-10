from urllib.parse import quote_plus
from pymongo import MongoClient

# Define your MongoDB URI with the correct username and escaped password
username = 'pundit'
password = 'pundit@2035P#'
escaped_password = quote_plus(password)
uri = f"mongodb+srv://{username}:{escaped_password}@atlascluster.nep04rx.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri)

db = client.myBlogs

blogsCollection = db['my blogs']

# Create a new client and connect to the server
try:
    client = MongoClient(uri)
    client.admin.command('ping')  # Send a ping to confirm a successful connection
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
