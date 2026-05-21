from operations import (
    add_book,
    view_books,
    issue_book,
    return_book,
    add_member,
    view_members,
    delete_member,
    view_issued_books
)

def menu():
    while True:
        print("\n==========  Library Management System ==========")
        print("1. Add Book")
        print("2. View Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Add Member")
        print("6. View Members")
        print("7. Delete Member")
        print("8. View Issued Books")
        print("9. Exit")
        print("=================================================")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                add_book()

            elif choice == 2:
                view_books()

            elif choice == 3:
                issue_book()

            elif choice == 4:
                return_book()

            elif choice == 5:
                add_member()

            elif choice == 6:
                view_members()

            elif choice == 7:
                delete_member()

            elif choice == 8:
                view_issued_books()

            elif choice == 9:
                print(" Exiting... Thank you!")
                break

            else:
                print(" Invalid choice! Please select 1-9.")

        except ValueError:
            print(" Please enter a valid number!")

        except Exception as e:
            print(f" Error: {e}")

if __name__ == "__main__":
    menu()