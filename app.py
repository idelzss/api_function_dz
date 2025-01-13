from typing import List
from fastapi import FastAPI, HTTPException
from schema import UserSchema
from database.base import session
from database.User_base import User
from utils_bcrypt import verify_password, hash_password




app = FastAPI()


@app.post("/register")
async def registration(user: UserSchema):
    hashed_password = hash_password(user.password)
    new_user = User(
        username=user.username,
        email=user.email,
        password=hashed_password
    )

    session.add(new_user)
    session.commit()
    return {"message": "User registered successfully"}


@app.post("/login")
async def login(user: UserSchema):
    db_user = session.query(User).filter(User.username == user.username,
                                         User.email == user.email
                                         ).first()

    if not db_user or not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid username or password or email")

    return {"message": f"Welcome, {user.username}!"}
