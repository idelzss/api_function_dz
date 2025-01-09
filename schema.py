from pydantic import BaseModel, EmailStr
from typing import Optional



class UserSchema(BaseModel):
    username: str
    email: EmailStr
    age: int


class UpdateUser(BaseModel):
    username: Optional[str]
    email: Optional[EmailStr]
    age: Optional[int]




