from datetime import datetime, timedelta
from fastapi import Response, HTTPException, status
from models.user import User as UserModel, LoginModel
from schemas.user import User as UserSchema
from utils.utils import hash_password, verify_paasword
from utils.utils import create_access_token, verify_token as token_verify

from db.user import find_user, add_user
from typing import Union, Dict, Optional, Any
from jose import JWTError
import uuid


def signup(body: UserModel):
    def c_signup(body: UserModel):
        uid = uuid.uuid4()
        hashed_password = hash_password(body.password)
        new_user = UserSchema(id=uid, email=body.email, name=body.name, password=hashed_password)
        response = add_user(new_user=new_user)
        return response

    return c_signup


def login():
    def c_login(body: LoginModel, response: Response) -> Union[
        HTTPException, Dict[str, Union[Dict[str, Union[datetime, Any]], bool]]]:
        f_user = find_user(body.email)
        if not f_user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={
                "data": None,
                "status": False
            })
        if not verify_paasword(body.password, f_user.password):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={
                "data": None,
                "status": False
            })
        access_token = create_access_token({"id": str(f_user.id), "email": f_user.email, "name": f_user.name})
        created_at = datetime.utcnow()
        exp = datetime.utcnow() + timedelta(hours=1)
        response.status_code = status.HTTP_200_OK
        return {
            "data": {
                "access_token": access_token,
                "created_at": created_at,
                "exp": exp
            },
            "status": True
        }

    return c_login


def verify():
    def verify_token(token: str, response: Response):

        try:
            decoded = token_verify(token)
            response.status_code = status.HTTP_200_OK
            return {
                "data": decoded,
            }
        except JWTError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not valid token")

    return verify_token
