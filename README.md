### 📚 **My Django Books API**  

This is a simple project where we can **add, update, delete, and view books** using a web API. Think of it as a **digital bookshelf** where we can organize books and interact with them through code instead of a website.  

---

## 🏗 **Project Structure**  

📂 **my_django_books/** → This is the main project folder.  
📂 **book_project/** → This holds the main settings and configurations.  
📂 **books/** → This application contains:  

- 📄 **models.py** → Defines how a book looks | models (title, author, etc.).  
- 📄 **serializers.py** → Converts data model into JSON format.  
- 📄 **views.py** → Implements the API logic (Get, POST, PUT, Delete).  
- 📄 **urls.py** → Maps our API endpoints to the correct web address | to views.  
- 📂 **tests/** → Contains the unit tests for the API validation.  

---

## 🔥 **How It Works**  

### 1️⃣ **Book Model**  
- Each book has a **title, author, publication date, ISBN, and summary**.  
- The **ISBN** must be unique (no two books can have the same one).  
- The **publication date** must be in the past (no future books allowed!).  

### 2️⃣ **API Endpoints**  
These are like magic doors that let us interact with the books:  
- 🟢 **GET /api/books/** → See all books.  
- 🟢 **POST /api/books/** → Add a new book.  
- 🟢 **GET /api/books/{id}/** → See details of a single book.  
- 🟡 **PUT /api/books/{id}/** → Update a book’s details.  
- 🔴 **DELETE /api/books/{id}/** → Remove a book.  

### 3️⃣ **Validation & Rules**  
- ISBN must be **10 or 13 digits**.  
- Publication date must be **in the past**.  

### 4️⃣ **Unit Tests**  
- **tests** Technically written to make sure APIs work correctly.  
- The test checks if we can **add, view, update, and delete books**.  

---

## 🚀 **Why this Design**  

- **Django REST Framework (DRF)** → Makes it easy to create APIs.  
- **ModelViewSet** → Helps manage books with less code.  
- **DefaultRouter** → Automatically creates our URLs.  
- **Unit Tests** → Ensures everything works before using the API.  

---

## 🛠 **How to Run the Project**  

1️⃣ Open **Git Bash** or **VS Code Terminal**.  
2️⃣ Activate the virtual environment:  
   ```bash
   venv\Scripts\activate  (Windows)
   source venv/bin/activate  (Mac/Linux)
   ```
3️⃣ Install requirements:  
   ```bash
   pip install -r requirements.txt
   ```
4️⃣ Apply migrations (sets up the database):  
   ```bash
   python manage.py migrate
   ```
5️⃣ Start the server:  
   ```bash
   python manage.py runserver
   ```
6️⃣ Open Postman or visit:  
   ```
   http://127.0.0.1:8000/api/books/
   ```
