# 📚 Library Management System

A **Console-Based Library Management System** developed using **Python** and **MySQL**.  
This project helps manage books, members, and book transactions efficiently through a menu-driven interface.

It is designed for beginners and intermediate developers to understand:

- Python CRUD Operations
- MySQL Database Connectivity
- Modular Programming
- Database Management
- Real-world Project Structure

---

# 🚀 Features

## 📖 Book Management
- Add new books
- View all books
- Track available copies
- Update stock automatically

## 👤 Member Management
- Add new members
- View member details
- Delete members

## 🔄 Transaction Management
- Issue books to members
- Return books
- Track issued books
- View return status

## 🗄 Database Integration
- MySQL database connectivity
- SQL schema included
- Persistent data storage

---

# 🛠 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Backend Logic |
| MySQL | Database |
| mysql-connector-python | Python-MySQL Connectivity |
| SQL | Database Queries |

---

# 📂 Project Structure

```bash
Library-Management-System/
│
├── main.py             # Main menu-driven application
├── operations.py       # All library operations
├── db.py               # Database connection setup
├── schema.sql          # Database schema
├── requirements.txt   # Required dependencies
├── README.md           # Project documentation
└── .gitignore          # Ignore unnecessary files
```

---

# ⚙️ Installation & Setup

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/library-management-system-python.git
```

---

## 2️⃣ Navigate to Project Folder

```bash
cd library-management-system-python
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🗄 Database Setup

## Step 1: Open MySQL

Login to MySQL:

```bash
mysql -u root -p
```

---

## Step 2: Create Database

```sql
CREATE DATABASE library_db;
USE library_db;
```

---

## Step 3: Run Schema File

Execute:

```sql
SOURCE schema.sql;
```

OR

Open `schema.sql` in MySQL Workbench and run it.

---

# 🔧 Configure Database Connection

Open `db.py` and update your MySQL credentials:

```python
import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",
        database="library_db"
    )
```

---

# ▶️ Run the Project

```bash
python main.py
```

---

# 🖥 Sample Output

```text
========== Library Management System ==========
1. Add Book
2. View Books
3. Issue Book
4. Return Book
5. Add Member
6. View Members
7. Delete Member
8. View Issued Books
9. Exit
=================================================
```

---

# 📌 Functionalities Explained

## 📘 Add Book
Allows librarian/admin to add books into the system.

Stores:
- Title
- Author
- Total Copies
- Available Copies

---

## 📗 View Books
Displays all books in a formatted table.

Includes:
- Book ID
- Title
- Author
- Total Copies
- Available Copies

---

## 📕 Issue Book
Issues a book to a member if copies are available.

Automatically:
- Creates transaction entry
- Reduces available copies

---

## 📙 Return Book
Marks book as returned.

Automatically:
- Updates return date
- Increases available copies

---

## 👥 Member Management
Manage library members efficiently.

Includes:
- Add Member
- View Members
- Delete Member

---

## 📑 Issued Books Tracking
Tracks:
- Which member issued which book
- Issue Date
- Return Date
- Return Status

---

# 🗃 Database Tables

## 📚 Books Table

| Column | Description |
|--------|-------------|
| book_id | Unique Book ID |
| title | Book Title |
| author | Author Name |
| total_copies | Total Copies |
| available_copies | Available Copies |

---

## 👤 Members Table

| Column | Description |
|--------|-------------|
| member_id | Unique Member ID |
| name | Member Name |
| phone | Contact Number |

---

## 🔄 Book_Issued Table

| Column | Description |
|--------|-------------|
| transaction_id | Transaction ID |
| book_id | Book Reference |
| member_id | Member Reference |
| issue_date | Issue Date |
| return_date | Return Date |

---

# 📸 Project Workflow

```text
Add Book → Add Member → Issue Book → Return Book → Track Transactions
```

---

# 💡 Concepts Used

- Python Functions
- Exception Handling
- MySQL CRUD Operations
- SQL Joins
- Modular Programming
- Database Relationships
- Transaction Management

---

# 🔐 Important Note

Do NOT upload your actual database password to GitHub.

Use environment variables or placeholder values like:

```python
password="your_password"
```

---

# 📦 requirements.txt

```txt
mysql-connector-python
```

---

# 🌟 Future Enhancements

Here are some features planned for future versions:

- 🔍 Search Books
- 🔐 Admin Login Authentication
- 💰 Fine Calculation System
- 📅 Due Date Tracking
- 📧 Email Notifications
- 🖥 GUI using Tkinter
- 🌐 Web Version using Flask/Django
- 📊 Analytics Dashboard
- 📁 Export Reports to CSV/PDF
- 🔄 REST API Integration

---

# 🎯 Learning Outcomes

This project is useful for learning:

- Real-world Python project structure
- Database connectivity
- SQL query execution
- CRUD application development
- Backend fundamentals

Perfect for:
- College Projects
- Resume Building
- Internship Applications
- Beginner Backend Practice

---

# 🤝 Contributing

Contributions are welcome.

If you want to improve this project:

1. Fork the repository
2. Create a new branch
3. Make changes
4. Commit changes
5. Push to your branch
6. Create Pull Request

---

# 📜 License

This project is open-source and free to use for educational purposes.

---

# 👨‍💻 Author

## Riya Patel



---

---