from fastapi import APIRouter, HTTPException
from crud import user
from schema.user import User, UserCreate, UsersResponse
from typing import List
import asyncio

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


# @router.get("/", response_model=List[User])
# async def get_users():
#     users = user.get_users()
#     if users is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return users


@router.get("/", response_model=UsersResponse)
async def get_users_new():
    users = user.get_users()
    if users is None:
        raise HTTPException(status_code=404, detail="User not found")
    response_dict = {
        "Count": len(users),
        "Users": users
    }
    response_object = UsersResponse(**response_dict)
    response_object.wackify_user_names()
    return response_object


@router.get("/{user_id}", response_model=User)
async def get_user(user_id: int):
    user_data = user.get_user(user_id=user_id)
    if user_data is None:
        raise HTTPException(status_code=404, detail="User not found")
    user_data = User(**user_data)
    user_data.titlefi_name()
    return user_data


@router.post("/", response_model=User)
async def create_user(payload: UserCreate) -> User:
    user_response = user.add_user(payload)
    user_object = {
        "User_Id": user_response,
        "Email": payload.Email,
        "Name": payload.Name
    }
    return user_object




