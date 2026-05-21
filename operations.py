from db import get_connection
from datetime import date

def add_book():
    conn = get_connection()
    cursor = conn.cursor()

    title = input("Enter title: ")
    author = input("Enter author: ")
    copies = int(input("Enter copies: "))

    query = "INSERT INTO Books (title, author, total_copies, available_copies) VALUES (%s,%s,%s,%s)"
    cursor.execute(query, (title, author, copies, copies))

    conn.commit()
    print("Book added successfully")

    cursor.close()
    conn.close()


# def view_books():
#     conn = get_connection()
#     cursor = conn.cursor()

#     cursor.execute("SELECT * FROM Books")
#     for row in cursor.fetchall():
#         print(row)

#     cursor.close()
#     conn.close()
def view_books():
    from db import get_connection

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Books")
    books = cursor.fetchall()

    print("\n Available Books:\n")

    if not books:
        print("No books found.")
    else:
        # Table Header
        print("{:<10} {:<25} {:<20} {:<10} {:<10}".format(
            "Book ID", "Title", "Author", "Total", "Available"
        ))
        print("-" * 80)

        # Table Rows
        for book in books:
            book_id, title, author, total, available = book
            print("{:<10} {:<25} {:<20} {:<10} {:<10}".format(
                book_id, title[:24], author[:19], total, available
            ))

    cursor.close()
    conn.close()

def issue_book():
    conn = get_connection()
    cursor = conn.cursor()

    book_id = int(input("Enter book ID: "))
    member_id = int(input("Enter member ID: "))

    # Check availability
    cursor.execute("SELECT available_copies FROM Books WHERE book_id=%s", (book_id,))
    result = cursor.fetchone()

    if result and result[0] > 0:
        cursor.execute(
            "INSERT INTO Book_Issued (book_id, member_id, issue_date) VALUES (%s,%s,%s)",
            (book_id, member_id, date.today())
        )

        cursor.execute(
            "UPDATE Books SET available_copies = available_copies - 1 WHERE book_id=%s",
            (book_id,)
        )

        conn.commit()
        print("Book issued")
    else:
        print("Book not available")

    cursor.close()
    conn.close()


def return_book():
    conn = get_connection()
    cursor = conn.cursor()

    transaction_id = int(input("Enter transaction ID: "))

    cursor.execute(
        "UPDATE Book_Issued SET return_date=%s WHERE transaction_id=%s",
        (date.today(), transaction_id)
    )

    cursor.execute(
        "UPDATE Books SET available_copies = available_copies + 1 WHERE book_id = (SELECT book_id FROM Book_Issued WHERE transaction_id=%s)",
        (transaction_id,)
    )

    conn.commit()
    print("Book returned")

    cursor.close()
    conn.close()

def add_member():
    from db import get_connection

    conn = get_connection()
    cursor = conn.cursor()

    name = input("Enter member name: ")
    phone = input("Enter phone: ")

    query = "INSERT INTO Members (name, phone) VALUES (%s, %s)"
    cursor.execute(query, (name, phone))

    conn.commit()
    print("Member added successfully")

    cursor.close()
    conn.close()

def view_members():
    from db import get_connection

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Members")
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    conn.close()

def delete_member():
    from db import get_connection

    conn = get_connection()
    cursor = conn.cursor()

    member_id = int(input("Enter member ID to delete: "))

    cursor.execute("DELETE FROM Members WHERE member_id=%s", (member_id,))
    conn.commit()

    print(" Member deleted")

    cursor.close()
    conn.close()

def view_issued_books():
    from db import get_connection

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT 
        t.transaction_id,
        b.title,
        m.name,
        t.issue_date,
        t.return_date
    FROM book_Issued t
    JOIN Books b ON t.book_id = b.book_id
    JOIN Members m ON t.member_id = m.member_id
    ORDER BY t.issue_date DESC
    """

    cursor.execute(query)
    results = cursor.fetchall()

    print("\n Issued Books:\n")

    if not results:
        print("No records found.")
    else:
        for row in results:
            transaction_id, title, member, issue_date, return_date = row

            status = "Returned" if return_date else "Not Returned"

            print(f"""
Transaction ID : {transaction_id}
Book           : {title}
Issued To      : {member}
Issue Date     : {issue_date}
Return Date    : {return_date}
Status         : {status}
-----------------------------------------
""")

    cursor.close()
    conn.close()    