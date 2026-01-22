from fastapi import FastAPI, UploadFile, HTTPException, Form
from enum import Enum
from pydantic import BaseModel, EmailStr, ValidationError
from typing import Optional
app = FastAPI()
ALLOWED_TYPES = [
    "application/pdf",
    "application/msword",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
]
MAX_SIZE = 10 * 1024 * 1024  # 5 MB

# Image file types allowed
ALLOWED_IMAGE_TYPES = [
    "image/jpeg",
    "image/png",
    "image/gif",
    "image/webp"
]

# Mock database - Students
students_db = [
    {
        "id": 1,
        "name": "Ali Karimov",
        "bio": "Frontend dasturchi, Vue va React bilan ishlaydi",
        "website": "https://alikarimov.dev",
        "avatar": "avatars/ali.png"
    },
    {
        "id": 2,
        "name": "Vali Tursunov",
        "bio": "Backend developer, FastAPI va Django mutaxassisi",
        "website": "https://valitursunov.uz",
        "avatar": "avatars/vali.png"
    },
    {
        "id": 3,
        "name": "Dilshod Akramov",
        "bio": "Mobilograf va video montaj ustasi",
        "website": "https://dilshodmedia.uz",
        "avatar": "avatars/dilshod.png"
    },
    {
        "id": 4,
        "name": "Malika Ismoilova",
        "bio": "UI/UX dizayner, Figma va Adobe XD",
        "website": "https://malikadesign.com",
        "avatar": "avatars/malika.png"
    },
    {
        "id": 5,
        "name": "Jasur Xolmatov",
        "bio": "Python o'rganuvchi va Telegram bot developer",
        "website": "https://jasurbot.dev",
        "avatar": "avatars/jasur.png"
    }
]

@app.post("/upload-image")
async def upload_image(file: UploadFile):
    if file.content_type not in ALLOWED_TYPES:
        raise HTTPException(status_code=400, detail=f"faqat{ALLOWED_TYPES} ruxsat berilgan")
    
    contents = await file.read()
    if len(contents) > MAX_SIZE:
        raise HTTPException(status_code=400, detail="Fayl 10mbdan katta")
    await file.seek(0)
    
    return {
        "filename": file.filename,
        "size": len(contents),
        "type": file.content_type
    }




@app.post("/login")
async def login(username: str = Form(), password: str = Form()):
    return {"username": username}


@app.post("/registration")
async def registration(mail: EmailStr = Form(), password: str = Form()):
    return {"mail": mail, "message": "Siz ro'yhatdan o'tdingiz!!"}


# @app.put("/profile/{student_id}")
# async def update_profile(
#     student_id: int,
#     name: str = Form(min_length=1),
#     bio: str = Form(min_length=1),
#     website: str = Form(),
#     avatar: Optional[UploadFile] = None
# ):
#     """
#     Profil yangilash endpoint
#     - student_id: O'quvchi ID si
#     - name: O'quvchi ismi (majburiy)
#     - bio: O'quvchi haqida (majburiy)
#     - website: Veb-sayt (majburiy)
#     - avatar: Avatar rasm (ixtiyoriy, faqat rasm)
#     """
    
#     # O'quvchini topish
#     student = None
#     for s in students_db:
#         if s["id"] == student_id:
#             student = s
#             break
    
#     if not student:
#         raise HTTPException(status_code=404, detail=f"O'quvchi ID {student_id} topilmadi")
    
#     # Avatar faylni tekshirish (agar bo'lsa)
#     if avatar:
#         if avatar.content_type not in ALLOWED_IMAGE_TYPES:
#             raise HTTPException(
#                 status_code=400, 
#                 detail=f"Faqat rasm fayllari ruxsat berilgan: {', '.join(ALLOWED_IMAGE_TYPES)}"
#             )
        
#         contents = await avatar.read()
#         if len(contents) > MAX_SIZE:
#             raise HTTPException(status_code=400, detail="Rasm 10MB dan katta")
        
#         # Avatar fayl nomini saqlash
#         avatar_path = f"avatars/{student_id}_{avatar.filename}"
#     else:
#         avatar_path = student["avatar"]  # Eski avatar saqlanadi
    
#     # Profilni yangilash
#     student["name"] = name
#     student["bio"] = bio
#     student["website"] = website
#     student["avatar"] = avatar_path
    
#     return {
#         "message": "Profil muvaffaqiyatli yangilandi",
#         "student": student
#     }


# @app.get("/students/{student_id}")
# async def get_student(student_id: int):
#     """
#     O'quvchi profilini olish endpoint
#     - student_id: O'quvchi ID si
#     """
#     for student in students_db:
#         if student["id"] == student_id:
#             return student
#     raise HTTPException(status_code=404, detail=f"O'quvchi ID {student_id} topilmadi")


















































# books = [
#     {"id": 1, "title": "Python Asoslari", "muallif": "Alisher Qodirov"},
#     {"id": 2, "title": "FastAPI bilan Backend", "muallif": "Jasur Karimov"},
#     {"id": 3, "title": "Django Amaliyoti", "muallif": "Dilshod Aliyev"},
#     {"id": 4, "title": "Ma'lumotlar Bazasi Asoslari", "muallif": "Malika Tursunova"},
#     {"id": 5, "title": "Algoritmlar va Ma'lumotlar Tuzilmasi", "muallif": "Bekzod Rahmonov"},
#     {"id": 6, "title": "Web Dasturlash Asoslari", "muallif": "Shahnoza Ismoilova"},
#     {"id": 7, "title": "JavaScript 0 dan Boshlab", "muallif": "Azizbek Yo‘ldoshev"},
#     {"id": 8, "title": "HTML & CSS Mukammal Qo‘llanma", "muallif": "Nodira Karimova"},
#     {"id": 9, "title": "REST API Dizayni", "muallif": "Rustam Abduqodirov"},
#     {"id": 10, "title": "Backend Arxitekturasi", "muallif": "Ulug‘bek Xolmatov"},
#     {"id": 11, "title": "Frontend Frameworklar", "muallif": "Sevara Rasulova"},
#     {"id": 12, "title": "Git va GitHub Amaliyoti", "muallif": "Sardor Mamatov"},
#     {"id": 13, "title": "Linux Asoslari", "muallif": "Kamola Saidova"},
#     {"id": 14, "title": "Testlash va Debug", "muallif": "Otabek Mirzayev"},
#     {"id": 15, "title": "Dasturchilar Uchun Ingliz Tili", "muallif": "Ziyoda Yusupova"}
# ]

# class Book(BaseModel):
#     id: int
#     title: str
#     muallif: str
    
# @app.get("/books", status_code=status.HTTP_200_OK)
# async def get_books(start: int = 0, end: int = 5):
#     return {
#         "total": len(books[start:end]),
#         "start": start,
#         "end": end,
#         "books": books[start:end]
#     }




# @app.post("/login")
# def login(username: str = Form(), password: str = Form()):
#     return {"username": username}


# @app.post("/register")
# def register(
#     username: str = Form(min_length=3, max_length=20),
#     email: str = Form(),
#     password: str = Form(min_length=8)
# ):
#     return {
#         "username": username,
#         "email": email,
#         "message": "Ro'yxatdan o'tdingiz"
#     }

# @app.post("/upload")
# def upload_file(file: UploadFile):
#     return {
#         "filename": file.filename,
#         "content_type": file.content_type,
#         "size": file.size
#     }


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
    


















# result = []

# @app.post("/book/", )
# async def add_book(book: Book):
#     result = book.dict





































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


# students = [
#     {
#         "id": 1,
#         "name": "Ali Valiyev",
#         "age": 20,
#         "contact": {
#             "phone": "+998901234567",
#             "email": "ali@gmail.com",
#             "address": "Farg'ona viloyati, Uchko‘prik tumani"
#         }
#     },
#     {
#         "id": 2,
#         "name": "Vali Aliyev",
#         "age": 22,
#         "contact": {
#             "phone": "+998933456789",
#             "email": "vali@mail.com",
#             "address": "Toshkent shahri, Chilonzor tumani"
#         }
#     },
#     {
#         "id": 3,
#         "name": "Laylo Karimova",
#         "age": 19,
#         "contact": {
#             "phone": "+998977654321",
#             "email": "laylo@gmail.com",
#             "address": "Andijon viloyati"
#         }
#     }
# ]

# class Book(BaseModel):
#     title: str = Field(min_length=1, max_length=200)
#     author: str
#     year: int
#     isbn: Optional[str] = None
#     page: Optional[int] = Field(gt=0)


# class Contacts(BaseModel):
#     phone: str
#     email: str
#     address: str
    
    
# class Student(BaseModel):
#     id: int
#     name: str = Field(gt=12)
#     age: int
#     contact: Contacts

# @app.get("/books")
# async def get_books():
#     return books

# @app.post("/create/book")
# async def create_book(book:Book):
#     books.append(book.dict())
#     return books



# @app.get("/students")
# async def get_students():
#     return students

# @app.post("/create/student")
# async def students_book(student:Student):
#     students.append(student.dict())
#     return students



# orders = [
#     {
#         "id": 1,
#         "order_name": "Burger + Cola",
#         "customer": {
#             "id": 101,
#             "name": "Ali Valiyev",
#             "phone": "+998901234567"
#         },
#         "restaurant": {
#             "id": 1,
#             "name": "Burger House",
#             "address": "Toshkent, Chilonzor"
#         },
#         "status": "pending"   # pending | preparing | delivered | canceled
#     },
#     {
#         "id": 2,
#         "order_name": "Pizza Pepperoni",
#         "customer": {
#             "id": 102,
#             "name": "Laylo Karimova",
#             "phone": "+998977654321"
#         },
#         "restaurant": {
#             "id": 2,
#             "name": "Italiano Pizza",
#             "address": "Farg'ona"
#         },
#         "status": "preparing"
#     },
#     {
#         "id": 3,
#         "order_name": "Lavash + Fries",
#         "customer": {
#             "id": 103,
#             "name": "Vali Aliyev",
#             "phone": "+998933456789"
#         },
#         "restaurant": {
#             "id": 3,
#             "name": "Street Food",
#             "address": "Andijon"
#         },
#         "status": "delivered"
#     }
# ]


# class Customer(BaseModel):
#     id: int
#     name: str
#     phone: str

# class Restaurant(BaseModel):
#     id: int
#     name: str
#     address: str

# class Order(BaseModel):
#     id: int
#     order_name: str
#     customer: Customer
#     restaurant: Restaurant
#     status: str


# class OrderStatus(BaseModel):
#     status: str


# @app.get("/orders")
# async def get_orders():
#     return orders



# @app.put("/orders/{order_id}/status")
# async def update_order_status(order_id: int, order_status: OrderStatus):
#     for idx, existing_order in enumerate(orders):
#         if existing_order["id"] == order_id:
#             orders[idx]["status"] = order_status.status
#             return orders[idx]
#     return {"error": "Buyurtma topilmadi"}













# class User(BaseModel):
#     id: int
#     name: str
#     email: str
#     password: str
#     is_admin: bool


# @app.post("/create/user", response_model=User, response_model_exclude={"password"})
# async def create_user(user: User):
#     return user




