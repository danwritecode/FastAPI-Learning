from fastapi import APIRouter, HTTPException
from crud import user
from schema.user import User
import asyncio

router = APIRouter(
    prefix="/user",
    tags=["user"],
)


@router.get("/{user_id}", response_model=User)
async def get_user(user_id: int):
    user_data = user.get_user(user_id=user_id)
    if user_data is None:
        raise HTTPException(status_code=404, detail="User not found")
    user_data = User(**user_data)
    user_data.titlefi_name()
    return user_data

@router.get("/delay/{user_id}", response_model=User)
async def get_user(user_id: int):
    await asyncio.sleep(3)
    user_data = user.get_user(user_id=user_id)
    if user_data is None:
        raise HTTPException(status_code=404, detail="User not found")
    user_data = User(**user_data)
    user_data.titlefi_name()
    return user_data



