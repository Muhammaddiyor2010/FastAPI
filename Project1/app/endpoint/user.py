from datetime import timedelta
from typing import Optional

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from ..core.models import Users
from ..core.db import get_db
from ..schema.schema import UserCreate, UserResponse, Token
from ..internal.user import (
    get_password_hash,
    get_current_active_user,
    authenticate_user,
    create_access_token,
    create_refresh_token,
    get_all_user,
)
from ..config import ACCESS_TOKEN_EXPIRE_MINUTES


user_router = APIRouter()


@user_router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(Users).filter(Users.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email allaqachon ro'yxatdan o'tgan")

    hashed_password = get_password_hash(user.password)
    new_user = Users(
        email=user.email,
        username=user.username,
        name=user.name,
        hashed_password=hashed_password,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@user_router.post("/login", response_model=Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Noto'g'ri email yoki parol",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    refresh_token =  create_refresh_token(
        data={"sub": user.email}
    )

    return {"refresh_token": refresh_token,"access_token": access_token, "token_type": "bearer"}


@user_router.get("/me", response_model=UserResponse)
def read_users_me(current_user: Users = Depends(get_current_active_user)):
    return current_user


@user_router.get("/protected")
def protected_route(current_user: Users = Depends(get_current_active_user)):
    return {"message": f"Salom, {current_user.username}!", "user_id": current_user.id}

@user_router.get("/get_users")
def get_all_users(db: Session = Depends(get_db)):
    users = get_all_user(db = db)
    return users