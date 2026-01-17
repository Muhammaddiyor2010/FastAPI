from fastapi import FastAPI,status
from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional
app = FastAPI()
books = [
    {
        "title": "Python Asoslari",
        "author": "Ali",
        "status": True,
        "min_year": 2018,
        "max_year": 2022,
        "comments": ["Zo'r kitob", "Boshlovchilar uchun juda yaxshi"]
    },
]

students = [
    {
        "id": 1,
        "name": "Ali Valiyev",
        "age": 20,
        "contact": {
            "phone": "+998901234567",
            "email": "ali@gmail.com",
            "address": "Farg'ona viloyati, Uchko‘prik tumani"
        }
    },
    {
        "id": 2,
        "name": "Vali Aliyev",
        "age": 22,
        "contact": {
            "phone": "+998933456789",
            "email": "vali@mail.com",
            "address": "Toshkent shahri, Chilonzor tumani"
        }
    },
    {
        "id": 3,
        "name": "Laylo Karimova",
        "age": 19,
        "contact": {
            "phone": "+998977654321",
            "email": "laylo@gmail.com",
            "address": "Andijon viloyati"
        }
    }
]

class Book(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    author: str
    year: int
    isbn: Optional[str] = None
    page: Optional[int] = Field(gt=0)


class Contacts(BaseModel):
    phone: str
    email: str
    address: str
    
    
class Student(BaseModel):
    id: int
    name: str = Field(gt=12)
    age: int
    contact: Contacts

@app.get("/books")
async def get_books():
    return books

@app.post("/create/book")
async def create_book(book:Book):
    books.append(book.dict())
    return books



@app.get("/students")
async def get_students():
    return students

@app.post("/create/student")
async def students_book(student:Student):
    students.append(student.dict())
    return students



orders = [
    {
        "id": 1,
        "order_name": "Burger + Cola",
        "customer": {
            "id": 101,
            "name": "Ali Valiyev",
            "phone": "+998901234567"
        },
        "restaurant": {
            "id": 1,
            "name": "Burger House",
            "address": "Toshkent, Chilonzor"
        },
        "status": "pending"   # pending | preparing | delivered | canceled
    },
    {
        "id": 2,
        "order_name": "Pizza Pepperoni",
        "customer": {
            "id": 102,
            "name": "Laylo Karimova",
            "phone": "+998977654321"
        },
        "restaurant": {
            "id": 2,
            "name": "Italiano Pizza",
            "address": "Farg'ona"
        },
        "status": "preparing"
    },
    {
        "id": 3,
        "order_name": "Lavash + Fries",
        "customer": {
            "id": 103,
            "name": "Vali Aliyev",
            "phone": "+998933456789"
        },
        "restaurant": {
            "id": 3,
            "name": "Street Food",
            "address": "Andijon"
        },
        "status": "delivered"
    }
]


class Customer(BaseModel):
    id: int
    name: str
    phone: str

class Restaurant(BaseModel):
    id: int
    name: str
    address: str

class Order(BaseModel):
    id: int
    order_name: str
    customer: Customer
    restaurant: Restaurant
    status: str


class OrderStatus(BaseModel):
    status: str


@app.get("/orders")
async def get_orders():
    return orders



@app.put("/orders/{order_id}/status")
async def update_order_status(order_id: int, order_status: OrderStatus):
    for idx, existing_order in enumerate(orders):
        if existing_order["id"] == order_id:
            orders[idx]["status"] = order_status.status
            return orders[idx]
    return {"error": "Buyurtma topilmadi"}





















# result = []

# @app.post("/book/", )
# async def add_book(book: Book):
#     result = book.dict


































# @app.get("/books")
# async def get_books(limit: int = 5):
#     result= []
#     if limit > len(books):
#         return {f"size" :len(books), "result": books}
    

# @app.get("/book_search")
# async def search_book(name: str):
#     result = []
#     for book in books:
#         if book["title"] == name:
#             result.append(book)
#             return {f"size": len(result), "result": result}

#     return {"detail": "Kitob topilmadi"}

# @app.get("/book_year_search")
# async def search_book_year(min_year: int, max_year: int):
#     result = []
#     for book in books:
#         if book["min_year"] > min_year and book["max_year"] < max_year:
#             result.append(book)
#             return {f"size": len(result), "result": result}
            
    
# @app.get("/book_search", status_code=status.HTTP_200_OK)
# async def search_book(name: str):
#     result = []
#     for book in books:
#         if book["title"] == name:
#             return f"Kitob nomi {book['title']}"     
#         return "xato" 
    



















































# @app.get("/books", status_code=status.HTTP_200_OK)
# def get_books():
#     return books



# @app.get("/books/{book_id}", status_code=status.HTTP_200_OK)
# def get_book(book_id: int):
#     for book in books:
#         if book["id"] == book_id:
#             return book
#     return {"error": "Book not found"}

# @app.post("/books", status_code=status.HTTP_201_CREATED)
# def add_book(book: object):
#     books.append(book)
#     return book



# @app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_book(id: int):
#     for index, book in enumerate(books):
#         if book["id"] == id:
#             books.pop(index)
#         return None










# students = [
#     {
#         "id": 1,
#         "name": "Student 1",
#         "fan": [
#             {"name": "matematika", "baxo": 5},
#             {"name": "adabiyot", "baxo": 4},
#             {"name": "kimyo", "baxo": 6},
#             {"name": "fizika", "baxo": 9},
#             {"name": "biologiya", "baxo": 3},
#         ]
#     },
#     {
#         "id": 2,
#         "name": "Student 2",
#         "fan": [
#             {"name": "matematika", "baxo": 5},
#             {"name": "kimyo", "baxo": 8}
#         ]
#     }
# ]


# @app.get("/", status_code=status.HTTP_200_OK)
# def home():
#     return {"message": "healthy"}



# @app.get("/student/{id}", status_code=status.HTTP_200_OK)
# def get_student(id:int):
#     for student in students:
#         if student["id"] == id:
#             return student
        
#     return {"xato": "student is not defined"}

# @app.get("/student/id/{id}/subject/{fan}", status_code=status.HTTP_200_OK)
# def get_student_grade(id:int, fan:str):
#     for student in students:
#         if student["id"] == id:
#             for f in student["fan"]:
#                 if f["name"] == fan:
#                    return {
#                         "student": student["name"],
#                         "fan": fan,
#                         "baho": f["baxo"]
#                     }
#             return {"xato":"Fan topilmadi"}
#         return {"xato": "Student topilmadi"}
            





    
#     for i in range(limit):
#         result.append(books[i])
#     return  {f"size" :len(result), "result": result}


# @app.get("/books/{book_id}/comments")
# def get_user_posts(
#     book_id: int,           # Path parameter
#     status: bool = True,  # Query parameter
#     limit: int = 10          # Query parameter
    
# ):
#     for i in books:
#         if i["id"] == book_id and status == status:
#             return i
#         else:
#           return {"msg": "Bu kitob uchun commentlar mavjud emas"}
#     return {
#         "book_id": book_id,
#         "status": status,
#         "limit": limit
#     }


