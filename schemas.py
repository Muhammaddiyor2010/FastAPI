from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
class BookBase(BaseModel):
    title: str
    author: str
    stock: int
    price: float
    isbn: int
class BookSchema(BookBase):
    id : int


    class Config:
        orm_mode = True
class BookUpdate(BookBase):
    pass
    
class OrderSchema(BaseModel):
    id: int
    user_id: int
    total: int
    status: str

    class Config:
        orm_mode = True
    
   
    
    
class OrderItemSchema(BaseModel):
    id:int
    order_id:int
    product_id:int
    quantity:int
    price:float

    class Config:
        orm_mode = True
        
    

    
    
    # class OrderItem(Base):
    # __tablename__ = "Orderitem"
    # id =  Column(Integer, primary_key=True, unique=True)
    # order_id =  Column(Integer, unique=True)
    # prduct_id =  Column(Integer, unique=True)
    # quantity = Column(Integer)
    # price = Column(Float)
    
    
# class ProductBase(BaseModel):
#     name: str = Field(..., max_length=200)
#     description: Optional[str] = None
#     price: int = Field(..., ge=0)
#     stock: int = Field(0, ge=0)
#     category: Optional[str] = None


# class ProductCreate(ProductBase):
#     pass


# class ProductUpdate(BaseModel):
#     name: Optional[str] = Field(None, max_length=200)
#     description: Optional[str] = None
#     price: Optional[int] = Field(None, ge=0)
#     stock: Optional[int] = Field(None, ge=0)
#     category: Optional[str] = None


# class ProductOut(ProductBase):
#     id: int
#     created_at: Optional[datetime]

#     class Config:
#         orm_mode = True
#         schema_extra = {
#             "example": {
#                 "id": 1,
#                 "name": "Smartphone",
#                 "description": "High-end smartphone",
#                 "price": 799,
#                 "stock": 10,
#                 "category": "phones",
#                 "created_at": "2026-01-29T12:34:56"
#             }
#         }
