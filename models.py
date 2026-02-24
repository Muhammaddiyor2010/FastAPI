from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, unique=True)
    title = Column(String)
    author = Column(String)
    stock = Column(Integer)
    price = Column(Float)
    isbn = Column(Integer)
    
class Order(Base):
    __tablename__ = "order"
    id =  Column(Integer, primary_key=True, unique=True)
    user_id =  Column(Integer, unique=True)
    total = Column(Integer)
    status = Column(String)
    created_at = Column(DateTime)
    
class OrderItem(Base):
    __tablename__ = "Orderitem"
    id =  Column(Integer, primary_key=True, unique=True)
    order_id =  Column(Integer, unique=True)
    product_id =  Column(Integer, unique=True)
    quantity = Column(Integer)
    price = Column(Float)
    
# class User(Base):
#     __tablename__ = "users"

#     id = Column(Integer, primary_key=True, index=True)
#     email = Column(String, unique=True, index=True)
#     name = Column(String)
#     hashed_password = Column(String)
#     is_active = Column(Boolean, default=True)
#     created_at = Column(DateTime, default=datetime.utcnow)

#     # no relationships defined here to avoid unresolved references


# class Category(Base):
#     __tablename__ = "categories"
    
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, unique=True, index=True)
#     description = Column(String)
#     created_at = Column(DateTime, default=datetime.utcnow)
    
    
# class Product(Base):
#     __tablename__ = "products"
    
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True)
#     description = Column(String)
#     price = Column(Integer, index=True)
#     stock = Column(Integer, index=True)
#     category = Column(String, index=True)
#     created_at = Column(DateTime, default=datetime.utcnow)
