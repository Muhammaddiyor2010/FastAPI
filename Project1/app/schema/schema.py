from pydantic import BaseModel, EmailStr
from typing import Optional

from datetime import datetime


class PostBase(BaseModel):
    title: str
    content: str


class PostResponse(BaseModel):
    id: int
    title: str
    content: str
    published: bool
    created_at: datetime
    views: int

    class Config:
        from_attributes = True


class UserCreate(BaseModel):
    email: EmailStr
    name: str
    username: Optional[str] = None
    password: str


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    name: str
    username: Optional[str] = None
    is_active: bool

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str
    refresh_token: str


class TokenData(BaseModel):
    email: Optional[str] = None