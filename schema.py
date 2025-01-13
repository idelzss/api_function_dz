from pydantic import BaseModel, EmailStr, validator
from typing import Optional



class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str

    @validator("username")
    def username_must_be_longer_then_3_but_short_then_20(cls, value):
        if 3 >= len(value) >= 20:
            raise ValueError("username must be longer then 3 but short then 20!")
        return value

    @validator("password")
    def password_must_be_longer_then_8(cls, value):
        if len(value) <= 8:
            raise ValueError("password must be longer then 8!")
        return value








