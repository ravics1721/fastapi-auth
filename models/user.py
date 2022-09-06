from datetime import datetime
from pydantic import BaseModel
from typing import Union


class User(BaseModel):
    email: str
    name: str
    password: str


class LoginModel(BaseModel):
    email: str
    password: str




class SignupResponse(BaseModel):
    message: str
