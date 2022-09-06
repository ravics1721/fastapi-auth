from fastapi import APIRouter, Depends, Response
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from models.user import User, LoginModel
from controllers.controllers import signup, login, verify

api_v1 = APIRouter(prefix="/api/v1")


@api_v1.get("/")
def v1():
    return {"message": "Version 1 API routes"}


@api_v1.post("/signup")
def signup(body: User, c_signup=Depends(signup)):
    return c_signup(body=body)


@api_v1.post("/login")
def login(body: LoginModel, response: Response, c_login=Depends(login)):
    return c_login(body=body, response=response)


authscheme = HTTPBearer()


@api_v1.get("/verify")
def verify(response: Response, token: HTTPAuthorizationCredentials = Depends(authscheme),
           validate_token=Depends(verify)):
    return validate_token(token.credentials, response)
