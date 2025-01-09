from typing import List
from fastapi import FastAPI, HTTPException
from schema import UserSchema, UpdateUser
from database.base import session
from database.User_base import User



app = FastAPI()


@app.get("/users")
async def get_users():
    users = session.query(User).all()
    return users


@app.post("/users")
async def create_user(user_data: UserSchema):
    new_user = User(
        username=user_data.username,
        email=user_data.email,
        age=user_data.age

    )
    session.add(new_user)
    session.commit()
    return {"message": "successful!"}

@app.put("/users/{user_id}")
async def update_user(user_id: int, update_user: UpdateUser):
    user = session.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    for key, value in update_user.dict(exclude_unset=True).items():
        setattr(user, key, value)

    session.commit()
    session.refresh(user)
    return user


@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
     user = session.query(User).filter(User.id == user_id).first()
     if not user:
         raise HTTPException(status_code=404, detail="User not found")

     session.delete(user)
     session.commit()
     return {"message": "successful!"}

