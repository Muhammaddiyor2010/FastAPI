from typing import Union
from sqlalchemy import or_
from sqlalchemy.orm import Session
from models import Book, Order, OrderItem
from schemas import BookSchema, OrderItemSchema, OrderSchema, BookBase, BookUpdate


def get_books(db: Session):
    return db.query(Book).filter(Book.stock > 0).all()
def get_book(db: Session, id: int):
    return db.query(Book).filter(Book.id == id).first()

def delete_book(db: Session, id: int):
    book = db.query(Book).filter(Book.id == id).first()
    
    if not book:
        return None   
    
    db.delete(book)
    db.commit()
    return book

def update_book(db: Session, id: int, book: BookUpdate):
    db_book = db.query(Book).filter(Book.id == id).first()
    if not db_book:
        return None

    update_data = book.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_book, key, value)

    db.commit()
    db.refresh(db_book)
    return db_book
    
def get_orders(db: Session):
    return db.query(Order).all()


def get_order_items(db: Session):
    return db.query(OrderItem).all()
def create_order(db:Session, order: OrderSchema):
    db_order = Order(
        id = order.id,
        user_id = order.user_id,
        total = order.total,
        status = order.status
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def create_item(db: Session, item: OrderItemSchema):
    db_item = OrderItem(
        id = item.id,
        order_id = item.order_id,
        product_id = item.product_id,
        quantity = item.quantity,
        price = item.price
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
def create_book(db: Session, book: BookSchema):
    db_book = Book(
        id = book.id,
        title = book.title,
        author = book.author,
        stock = book.stock,
        price = book.price,
        isbn = book.isbn
        
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book#





# def delete_product(db: Session, product_id: int):
#     db_product = db.query(Product).filter(Product.id == product_id).first()
#     if db_product:
#         db.delete(db_product)
#         db.commit()
#     return db_product


# def edit_product(db: Session, product_id: int, product: ProductUpdate):
#     db_product = db.query(Product).filter(Product.id == product_id).first()
#     if not db_product:
#         return None

#     update_data = product.dict(exclude_unset=True)
#     for key, value in update_data.items():
#         setattr(db_product, key, value)

#     db.commit()
#     db.refresh(db_product)
#     return db_product
