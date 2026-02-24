from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..core.db import get_db
from ..core.models import Users
from ..schema.schema import PostResponse, PostBase
from ..internal.posts import (
    get_all_posts,
    get_post_by_id,
    create_post,
    update_post,
    delete_post,
)
from ..internal.user import get_current_active_user


post_router = APIRouter()


@post_router.get("/posts", response_model=List[PostResponse])
def read_posts(db: Session = Depends(get_db)):

    return get_all_posts(db)


@post_router.get("/posts/{post_id}", response_model=PostResponse)
def read_post(post_id: int, db: Session = Depends(get_db)):

    post = get_post_by_id(db, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post topilmadi")
    return post


@post_router.post("/posts", response_model=PostResponse, status_code=status.HTTP_201_CREATED)
def create_post_endpoint(
    post: PostBase,
    db: Session = Depends(get_db),
    current_user: Users = Depends(get_current_active_user),
):
    return create_post(db, post)


@post_router.put("/posts/{post_id}", response_model=PostResponse)
def update_post_endpoint(
    post_id: int,
    post: PostBase,
    db: Session = Depends(get_db),
    current_user: Users = Depends(get_current_active_user),
):
    updated = update_post(db, post_id, post)
    if not updated:
        raise HTTPException(status_code=404, detail="Post topilmadi")
    return updated


@post_router.delete("/posts/{post_id}")
def delete_post_endpoint(
    post_id: int,
    db: Session = Depends(get_db),
    current_user: Users = Depends(get_current_active_user),
):
    success = delete_post(db, post_id)
    if not success:
        raise HTTPException(status_code=404, detail="Post topilmadi")
    return {"detail": "Post o'chirildi"}
