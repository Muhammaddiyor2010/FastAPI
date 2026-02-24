from sqlalchemy.orm import Session

from ..core.models import Post
from ..schema.schema import PostBase


def get_all_posts(db: Session):
    return db.query(Post).all()


def get_post_by_id(db: Session, post_id: int):
    return db.query(Post).filter(Post.id == post_id).first()


def create_post(db: Session, post: PostBase):
    new_post = Post(
        title=post.title,
        content=post.content,
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


def update_post(db: Session, post_id: int, post: PostBase):
    db_post = db.query(Post).filter(Post.id == post_id).first()
    if not db_post:
        return None
    db_post.title = post.title
    db_post.content = post.content
    db.commit()
    db.refresh(db_post)
    return db_post


def delete_post(db: Session, post_id: int):
    db_post = db.query(Post).filter(Post.id == post_id).first()
    if not db_post:
        return False
    db.delete(db_post)
    db.commit()
    return True
