import datetime

import mysql.connector
projectdb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='av@py2/ramsan',
    db="lms",
    autocommit=True
)
mydb=projectdb.cursor()

def logout():
    global current_user
    current_user = None
    print("\nLogged out successfull!")
    #mydb.close()
    login()
def admin_options():
    print("\n----- ADMIN OPTIONS -----")
    print("___________________________________________________________________________________________________________________________")

    print("1. View Books")
    print("2. View Users")
    print("3. Remove user")
    print("4. View order details")
    print("5. Logout")
    choice = input("Enter choice (1-5): ")
    if choice == "1":
        display_all_books()
    elif choice == "2":
        display_all_users()
    elif choice == "3":
        remove_user()
    elif choice == "4":
        display_order_details()
    elif choice == "5":
        logout()
    else:
        print("Invalid choice. Please try again.")
        admin_options()

def display_all_books():
    sql = "SELECT * FROM books"
    mydb.execute(sql)
    books = mydb.fetchall()

    print("\n{:<10} {:<80} {:<30} {:<25} {:<10} {:<10}".format("Book ID", "Title", "Author", "Category", "Quantity", "Price"))
    print("___________________________________________________________________________________________________________________________")

    for book in books:
        print("{:<10} {:<80} {:<30} {:<25} {:<10} {:<10}".format(book[0], book[1], book[2], book[3], book[4], book[5]))
    book_options()

def display_all_users():
    query = "SELECT * FROM users"
    mydb.execute(query)
    result = mydb.fetchall()
    print("\n{:<10} {:<20} {:<20} {:<20} ".format("User ID", "Username", "phone_no", "Email-ID"))
    print("___________________________________________________________________________________________________________________________")

    for user in result:
        print("{:<10} {:<20} {:<20} {:<20}".format(user[0], user[1], user[3], user[4]))
    admin_options()


def book_options():
    print("\n----- BOOK OPTIONS -----")
    print(
        "___________________________________________________________________________________________________________________________")

    print("1. Add Book")
    print("2. Update Book")
    print("3. Remove Book")
    print("4. Go Back")
    choice = input("Enter choice (1-4): ")
    if choice == "1":
        add_book()
    elif choice == "2":
        update_book()
    elif choice == "3":
        remove_book()
    elif choice == "4":
        admin_options()
    else:
        print("Invalid choice. Please try again.")
        book_options()


def user_options():
    print("\n----- USER OPTIONS -----")
    print("___________________________________________________________________________________________________________________________")
    print("1. Edit User")
    print("2. Search Book")
    print("3. Order Book")
    print("4. Show order details")
    print("5. Return Book")
    print("6. Remove Account")
    print("7. Logout")
    choice = input("Enter choice (1-7): ")
    if choice == "1":
        edit_user()
    elif choice == "2":
        search_book()
    elif choice == "3":
        order_book()
    elif choice == "4":
        show_order_details()
    elif choice == "5":
        return_book()
    elif choice =="6":
        remove_account()
    elif choice =="7":
        logout()
    else:
        print("Invalid choice. Please try again.")
        user_options()

def edit_user():
    print("\n----- UPDATE  -----")

    query = "SELECT * FROM users where user_id=%s"
    val=current_user
    mydb.execute(query,val)
    result = mydb.fetchall()
    print("\n{:<20} {:<20} {:<20} ".format( "Username", "phone_no", "Email-ID"))
    print("___________________________________________________________________________________________________________________________")

    for user in result:
        print(" {:<20} {:<20} {:<20}".format( user[1], user[3], user[4]))


    user_name = input("Enter User name: ")
    new_ph_no = input("Enter new phone number (press enter to skip): ")
    new_email = input("Enter new email (press enter to skip): ")

    if new_ph_no and new_email:
        sql = "UPDATE users SET phone_no = %s, email_id = %s WHERE username = %s"
        val = (new_ph_no, new_email, user_name)
        mydb.execute(sql, val)
    elif new_ph_no:
        sql = "UPDATE users SET phone_no = %s WHERE username = %s"
        val = (new_ph_no,user_name)
        mydb.execute(sql, val)
    elif new_email:
        sql = "UPDATE users SET email_id = %s WHERE username = %s"
        val = (new_email, user_name)
        mydb.execute(sql, val)
    else:
        print("No changes made.")
        user_options()
    mydb.fetchall()
    print(mydb.rowcount, "user(s) updated successfully.")
    print("\n{:<20} {:<20} {:<20} ".format("Username", "phone_no", "Email-ID"))
    print("___________________________________________________________________________________________________________________________")
    query1 = "SELECT * FROM users where user_id=%s"
    val1 = current_user
    mydb.execute(query1,val1)
    result = mydb.fetchall()
    for user in result:
        print(" {:<20} {:<20} {:<20}".format(user[1], user[3], user[4]))
    user_options()

def search_book():
    categories()
    bookname=input("\nEnter bookname or category:")
    # authorname=input("Enter authorname:")
    mydb.execute('use lms')
    mydb.execute('SELECT * FROM books WHERE book_name=%s OR category=%s',(bookname,bookname))
    books=mydb.fetchall()
    if not books:
        print("Not Exist")
    else:
        print("\n{:<10} {:<80} {:<30} {:<25} {:<10} {:<10}".format("Book ID", "Title", "Author", "Category", "Quantity","Price"))
        print(
            "___________________________________________________________________________________________________________________________")

        for book in books:
            print("{:<10} {:<80} {:<30} {:<25} {:<10} {:<10}".format(book[0], book[1], book[2], book[3], book[6], book[5]))
    user_options()
def categories():

    sql = "SELECT DISTINCT category FROM books"
    mydb.execute(sql)
    books = mydb.fetchall()

    print("\n{:<25}".format("Category"))
    print("___________________________________________________________________________________________________________________________")
    for book in books:
        print("{:<25}".format(book[0]))

def order_book():
    from datetime import date,timedelta
    print("\n----- Order BOOK -----")
    print("___________________________________________________________________________________________________________________________")

    book_id=input("Enter the BOOK ID: ")

    sql = "SELECT * FROM books WHERE book_id = %s"
    val = (book_id,)
    mydb.execute(sql, val)
    result = mydb.fetchone()
    if result is None:
        print("Id not found.")
    elif result[6]>0:
        userid=current_user[0]
        # print(userid)
        orderdate = date.today()
        returndate = orderdate + timedelta(days=15)
        sql = "INSERT INTO orders(user_id,book_id,order_date,return_date) VALUES (%s,%s,%s,%s)"
        val =(userid,book_id,orderdate,returndate)
        mydb.execute(sql,val)
        mydb.fetchall()

        new_qty=result[4]-1
        sql2="update books set balance_qty =%s where book_id= %s"
        values=(new_qty,book_id)
        mydb.execute(sql2,values)
        mydb.fetchall()
        f=0
        sql3="update orders set fine=%s where book_id=%s"
        val1=(f,book_id)
        mydb.execute(sql3,val1)
        print("\n",mydb.rowcount, "Book ordered successfully.\n")
        print("\nThe return date for the book is on or before :", returndate)

    else:
        print("\nRequested book is out of stock!!!!!")
    user_options()

def display_order_details():
    print("\n----- Show Orders  -----")
    print("___________________________________________________________________________________________________________________________")

    mydb.execute('use lms')
    mydb.execute('SELECT * FROM orders')
    result = mydb.fetchall()
    if not result:
        print("Not Exist")
    else:
        print("\n{:<10} {:<10} {:<10} {:<14} {:<15} {:<10}".format("Order ID","User ID", "Book ID", "Order Date", "Return Date", "Fine"))
        print(
            "___________________________________________________________________________________________________________________________")

        for order in result:
            print("{:<10} {:<10} {:<10} {}\t {}\t\t {:<10}".format(order[0],order[1],order[2], order[3], order[4],order[5]))
    admin_options()


def show_order_details():
    print("\n----- Show Orders  -----")
    print("___________________________________________________________________________________________________________________________")

    mydb.execute('use lms')
    mydb.execute('SELECT * FROM orders WHERE user_id=%s', (current_user))
    result = mydb.fetchall()
    if not result:
        print("No order exists for this user!!")
    else:
        print("\n{:<10} {:<10} {:<10} {:<14} {:<15}".format("Order ID","User ID", "Book ID", "Order Date", "Return Date"))
        print(
            "___________________________________________________________________________________________________________________________")

        for order in result:
            print("{:<10} {:<10} {:<10} {}\t {}\t\t ".format(order[0],order[1],order[2], order[3], order[4]))
    user_options()


def return_book():
    print("\n----- Book Return -----")
    print("___________________________________________________________________________________________________________________________")

    from datetime import date

    order_id = input("Enter the Order ID: ")
    return_date = date.today()

    sql = "SELECT * FROM orders WHERE order_id = %s"
    values = (order_id,)
    mydb.execute(sql, values)
    result = mydb.fetchone()

    if result is None:
        print("\nOrder not found.")
    else:
        return_date = date.today()
        if return_date > result[4]:
            # issue_date = result[3]
            expiry_date = result[4]
            today = date.today()
            days_overdue = (today - expiry_date).days
            fine_per_day = 1
            fine_amount = fine_per_day * days_overdue

            if fine_amount > 0:
                print(f"You have a fine of ${fine_amount} for {days_overdue} days overdue.")
                sql = "UPDATE orders SET fine = %s WHERE order_id = %s"
                values = (fine_amount, order_id)
                mydb.execute(sql, values)
                mydb.fetchall()

        sql = "DELETE FROM orders WHERE order_id = %s"
        values = (order_id,)
        mydb.execute(sql, values)
        mydb.fetchall()
        sql1 = "SELECT * FROM books WHERE book_id = %s"
        val1 = (result[2],)
        mydb.execute(sql1, val1)
        result1=mydb.fetchone()
        new_qty = result1[6] + 1
        sql2 = "update books set balance_qty =%s where book_id= %s"
        values = (new_qty, result[2])
        mydb.execute(sql2, values)
        mydb.fetchall()
        print("\nBook returned successfully.")

    user_options()




def remove_account():
    print("****Remove Account*****")
    print("___________________________________________________________________________________________________________________________")

    user_id =current_user[0]
    choice=input("Do you want to remove account? press 1.yes")
    if choice == "1":
        sql = "DELETE FROM users WHERE user_id = %s"
        values = (user_id,)
        mydb.execute(sql, values)
        mydb.fetchall()
        print("User removed successfully.")
    user_options()

def add_book():
    print("\n----- ADD BOOK -----")
    print("___________________________________________________________________________________________________________________________")

    book_id= input("Enter the BOOK ID: ")
    book_name = input("Enter book name: ")
    author_name = input("Enter author name: ")
    category= input("Enter the book category: ")
    quantity = input("Enter quantity: ")
    price= input("Enter the price of the book: ")


    sql = "INSERT INTO books (book_id, book_name, author_name, category, quantity, price) VALUES (%s,%s, %s, %s, %s,%s)"
    val = (book_id,book_name, author_name, category, quantity,price)
    mydb.execute(sql, val)
    mydb.fetchall()
    sql1="update books set balance_qty=%s where book_id=%s"
    val1=(quantity,book_id)
    mydb.execute(sql1,val1)
    print(mydb.rowcount, "book added successfully.")
    admin_options()



def update_book():
    print("\n----- UPDATE BOOK -----")
    print("___________________________________________________________________________________________________________________________")

    book_id = input("Enter the BOOK ID: ")
    # book_name = input("Enter book name: ")
    new_author_name = input("Enter new author name (press enter to skip): ")
    new_quantity = input("Enter new quantity (press enter to skip): ")


    if new_author_name and new_quantity:
        sql = "UPDATE books SET author_name = %s, quantity = %s WHERE book_id = %s"
        val = (new_author_name, new_quantity, book_id)
        mydb.execute(sql, val)
    elif new_author_name:
        sql = "UPDATE books SET author_name = %s WHERE book_id = %s"
        val = (new_author_name, book_id)
        mydb.execute(sql, val)
    elif new_quantity:
        sql = "UPDATE books SET quantity = %s WHERE book_id = %s"
        val = (new_quantity, book_id)
        mydb.execute(sql, val)
    else:
        print("No changes made.")
        admin_options()

    mydb.fetchall()
    print(mydb.rowcount, "Book(s) updated successfully.")
    admin_options()


def remove_book():
    book_id = input("Enter the BOOK ID: ")
    book_name = input("Enter title of the book to be removed: ")

    sql = "SELECT * FROM books WHERE book_id = %s"
    values = (book_id,)
    mydb.execute(sql, values)
    result = mydb.fetchone()
    if result is None:
        print("Book not found.")
    else:
        sql = "DELETE FROM books WHERE book_id = %s"
        values = (book_id,)
        mydb.execute(sql, values)
        mydb.fetchall()

        print(mydb.rowcount, "book removed successfully.")
    admin_options()

def remove_user():
    user_id = input("Enter user id of the user to be removed: ")

    sql = "SELECT * FROM users WHERE user_id = %s"
    values = (user_id,)
    mydb.execute(sql, values)
    result = mydb.fetchone()
    if result is None:
        print("User not found.")
    else:
        sql = "DELETE FROM users WHERE user_id = %s"
        values = (user_id,)
        mydb.execute(sql, values)
        mydb.fetchall()
        print("User removed successfully.")
    admin_options()

def create_account():
    username = input('Enter your name: ')
    phone_no = input('Enter your 10-digit mobile number: ')
    passwords =input('Enter your password: ')
    email_id = input('Enter your email: ')

    mydb.execute('SELECT user_id FROM users WHERE phone_no=%s AND email_id=%s', (phone_no, email_id))
    users = mydb.fetchone()
    if users is not None:
        print('User already exists.')
        return

    mydb.execute('INSERT INTO users (username, phone_no, email_id, passwords) VALUES (%s, %s, %s, %s)', (username, phone_no, email_id,passwords))
    mydb.fetchall()
    print('Account created successfully.')
    login()

def admin_login():
    global current_user
    username=input("enter your user name:")
    password=input("enter your password:")
    mydb.execute('use lms')
    mydb.execute('SELECT admin_id FROM admins WHERE username=%s AND passwords=%s',(username,password))

    admins=mydb.fetchone()
    if admins:
        current_user = admins
        print("Login successful!")
        admin_options()
    else:
        print("Incorrect username or password. Please try again.")
        admin_login()

def user_login():
    global current_user
    username = input("Enter your user name:")
    password = input("Enter your password:")
    mydb.execute('use lms')
    mydb.execute('SELECT user_id FROM users WHERE username=%s AND passwords=%s', (username, password))

    users = mydb.fetchone()
    if users:
        current_user=users

        print("\nLogin successful!")
        user_options()
    else:
        print("\nIncorrect username or password. Please try again or Create a new account.")

def login():
    print('\nWelcome to the Library Management System')
    print("___________________________________________________________________________________________________________________________")

    while True:
        print('\nPlease select an option:')
        print(
            "___________________________________________________________________________________________________________________________")

        print('1. User Login')
        print('2. Create New User Account')
        print('3. Admin Login')
        print('4. Exit')
        print(
            "___________________________________________________________________________________________________________________________")

        choice = input('Enter your choice (1/2/3/4): ')
        if choice == '1':
            user_login()
        elif choice=='2':
            create_account()
        elif choice == '3':
            admin_login()
        elif choice == '4':
            print('Thank you for using the Library Management System')
            print(
                "___________________________________________________________________________________________________________________________")

            break
        else:
            print('Invalid choice. Please try again.')
login()

