from fastapi import HTTPException
from pymongo import MongoClient
import os
from dotenv import load_dotenv
import bcrypt

# Load environment variables
load_dotenv()

# MongoDB Atlas connection
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
mongo_client = MongoClient(MONGO_URI)
db = mongo_client["ppc_goat_db"]
users_collection = db["users"]

async def register_user(name: str, email: str, password: str) -> dict:
    """Register a user with name and password hashing."""
    # Check if user already exists
    if users_collection.find_one({"email": email}):
        raise HTTPException(status_code=400, detail="Email already registered")

    # Hash the password using bcrypt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    
    # Store user in MongoDB
    user_data = {"name": name, "email": email, "password": hashed_password}
    users_collection.insert_one(user_data)
    
    return {"message": "Registration successful", "name": name, "email": email}

async def login_user(email: str, password: str) -> dict:
    """Log in a user by verifying email and password."""
    # Find user in MongoDB
    user = users_collection.find_one({"email": email})
    if not user:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    
    # Verify password using bcrypt
    if not bcrypt.checkpw(password.encode('utf-8'), user["password"]):
        raise HTTPException(status_code=401, detail="Invalid email or password")
    
    return {"message": "Login successful", "name": user.get("name"), "email": email}