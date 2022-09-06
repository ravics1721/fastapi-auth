from typing import Union, List, Dict
from schemas import user

user_stores: List[user.User] = []


def add_user(new_user: user.User, err=None) -> Dict[str, Union[str, bool]]:
    try:
        user_stores.append(new_user)
        return {
            "status": True,
            "message": 'Successfully added new user',
            "data": user_stores
        }
    except:
        return {
            "status": False,
            "message": 'Some error adding new user',
            "data": user_stores
        }


def find_user(email: str) -> Union[user.User, None]:
    result = None

    for a_user in user_stores:
        if a_user.email == email:
            result = a_user
            break

    return result
