from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from ..core.db import Base

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    
    username = Column(String)
    name = Column(String)

    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # posts = relationship("Post", back_populates="author")
    # comments = relationship("Comment", back_populates="author")

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)
    published = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    # author_id = Column(Integer, ForeignKey("users.id"))
    views = Column(Integer, default=0)
    # # Relationship
    # author = relationship("User", back_populates="posts")
    # comments = relationship("Comment", back_populates="post")



class Comment(Base):
    __tablename__ = "comment"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    published = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    # author_id = Column(Integer, ForeignKey("users.id"))
    # post_id = Column(Integer, ForeignKey("posts.id"))

    # author = relationship("User", back_populates="comments")
    # post = relationship("Post", back_populates="comments")
