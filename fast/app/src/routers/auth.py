from uuid import uuid4
from fastapi import APIRouter
from fastapi import FastAPI, status, HTTPException, Depends
from fastapi.responses import RedirectResponse
from fastapi.security import OAuth2PasswordRequestForm
from ..utils.schemas import UserOut, UserAuth, TokenSchema
from ..utils.auth import get_hashed_password
from ..utils.prisma import prisma 
from ..utils.auth import (
  get_hashed_password,
  verify_password,
  create_access_token,
)
from ..utils.deps import get_current_userId
router = APIRouter()

@router.get('/userInfo', summary='Get user details', response_model=UserOut)
async def get_me(userId: str = Depends(get_current_userId)):
    if (userId):
        user = await prisma.user.find_first(
            where={
                "id": userId
            }
        )
        return {"username": user.username, "name": user.name}

@router.post('/signup', summary="Create new user", response_model=UserOut)
async def create_user(data: UserAuth):
    user = await prisma.user.find_first(
    where={
      "username": data.username,
      }
    )

    if(user):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exists"
        )

    user = await prisma.user.create(
        {
            'username': data.username,
            'name': data.name,
            'password': get_hashed_password(data.password)
        }
    )
    return user

@router.post('/login', summary="Create access token for user", response_model=TokenSchema)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await prisma.user.find_unique(
        where={
            'username': form_data.username
        }
    )
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect credentials"
        )

    hashed_pass = user.password
    if not verify_password(form_data.password, hashed_pass):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect credentials"
        )
    
    return {
        "access_token": create_access_token(user.id),
    }
