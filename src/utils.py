import os
import time
import pymysql
from dotenv import load_dotenv
from typing import List

# General Utilities
def clear_screen():
    # Clearing screen is different depending on whether windows or unix-like
    os.system('cls' if os.name == 'nt' else 'clear')

def sql_execute(sql, data):
    # Load environment variables from .env file
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")

    # Establish a database connection
    connection = pymysql.connect(
        host,
        user,
        password,
        database
    )
    # A cursor is an object that represents a DB cursor,
    # which is used to manage the context of a fetch operation.
    cursor = connection.cursor()
    
    cursor.execute(sql, data)
    connection.commit()

    # Closes the cursor so will be unusable from this point 
    cursor.close()

    # Closes the connection to the DB, make sure you ALWAYS do this
    connection.close()

def sql_read(sql, data=None):
    # Load environment variables from .env file
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")

    # Establish a database connection
    connection = pymysql.connect(
        host,
        user,
        password,
        database
    )
    # A cursor is an object that represents a DB cursor,
    # which is used to manage the context of a fetch operation.
    cursor = connection.cursor()
    
    cursor.execute(sql, data)
    rows = cursor.fetchall()

    # Closes the cursor so will be unusable from this point 
    cursor.close()

    # Closes the connection to the DB, make sure you ALWAYS do this
    connection.close()

    return rows

def int_input_check(details: str):
    
        while True:
                value = input(details)
                if value == "":
                    return ""
                else:
                    try:
                        number = int(value)
                        return number
                    except ValueError:
                        print("\n \tInvalid input. Please try again...")

def float_input_check(details: str):

        while True:
            value = input(details)
            if value == "":
                return ""
            else:
                try:
                    number = float(value)
                    return number
                except ValueError:
                    print("\n \tInvalid input. Please try again...")

def upper_case_conversion(string: str):
    if string == "":
        return ""
    else:
        return " ".join([(i[0].upper() + i[1:].lower()) for i in string.split(" ")])
    # string = "small coffee"
    # newstring = []
    # for i in string.split(" "):
    #     i = (i[0].upper() + i[1:].lower())
    #     newstring.append(i)
    #     x = " ".join(newstring)
    # print(x)
    
    # list comprehension applied to combine code into one liner return

def task_choice(details: str):
    while True:
        user_choice = input(details).lower()
        if user_choice == 'y':
            return True
        elif user_choice == 'n':
            return False
        else:
            print("\n \tInvalid choice. Please try again...")


# Products Utilities
def view_all_products():
    
    sql = "SELECT product_id, name, price, stock FROM products"
    rows = sql_read(sql)
    print("\n \tList of Products: ")
    print(f"\t{'Id:' :<7} | {'Name:' :<20} | {'Price:' :<10} | {'Qty:' :<5} ")
    for row in rows:
        print(f"\t{row[0] :<7} | {str(row[1]) :<20} | {row[2] :<10} | {row[3] :<5}")

def view_unique_product(id_choice):
    
    sql = "SELECT product_id, name, price, stock FROM products WHERE product_id=%s"
    rows = sql_read(sql, id_choice)
    
    for row in rows:
        print(f"""
        [1]. - Name: {str(row[1])}
        [2]. - Price: {row[2]}
        [3]. - Qty: {row[3]}""")

def product_name_duplicate_check(details: str):
    
    while True:
        name = upper_case_conversion(input(details))
        sql = "SELECT name FROM products WHERE name=%s"
        data_check = sql_read(sql,name)
        if not data_check:
            return name
        else:
            print(f"\n \t{name} already exists. Please try again...")

def product_id_check(details: str):
    
    while True:
        id_choice = int_input_check(details)
        sql = "SELECT product_id FROM products WHERE product_id=%s"
        data_check = sql_read(sql, id_choice)
        if not data_check:
            print(f"\n \tProduct with Id: {id_choice} doesn't exists. Please try again...")
            continue
        else:
            return id_choice

def product_stock_check(product_id, details: str):
    
    while True:
        clear_screen()
        view_unique_product(product_id)
        qty_choice = int_input_check(details)
        sql = "SELECT stock FROM products WHERE product_id=%s"
        rows = sql_read(sql, product_id)
        for row in rows:
            qty_check = row[0] 
        if qty_choice > qty_check:
            print(f"\n \tThere isn't enough in stock. Please use smaller amount...")
            time.sleep(1)
            continue
        else:
            sql = """UPDATE products set stock = %s where product_id = %s"""
            reduced_stock = qty_check - qty_choice
            data = (reduced_stock, product_id)
            sql_execute(sql, data)
            return qty_choice


# Couriers Utilities
def view_all_couriers():
    
    sql = "SELECT courier_id, name, phone FROM couriers"
    rows = sql_read(sql)
    print("\n \tList of Couriers: ")
    print(f"\t{'Id:' :<7} | {'Name:' :<20} | {'Phone:' :<10} ")
    for row in rows:
        print(f"\t{row[0] :<7} | {str(row[1]) :<20} | {row[2] :<10} ")


def courier_id_check( details: str):
    
    while True:
        clear_screen()
        view_all_couriers()
        id_choice = int_input_check(details)
        sql = "SELECT courier_id FROM couriers WHERE courier_id=%s"
        data_check = sql_read(sql, id_choice)
        if not data_check:
            print(f"\n \tCourier with Id: {id_choice} doesn't exists. Please try again...")
        else:
            return id_choice


# Orders Utilities
def view_all_orders():
    
    sql = """SELECT orders.order_id, customers.customer_name, customers.customer_address, customers.customer_phone, 
                    couriers.courier_id, order_status.order_status, orders_products.product_id, orders_products.quantity
                FROM orders
                LEFT JOIN customers
                ON orders.customer_id = customers.customer_id
                LEFT JOIN couriers
                ON orders.courier_id = couriers.courier_id
                LEFT JOIN order_status
                ON orders.status_id = order_status.status_id
                LEFT JOIN orders_products
                ON orders.order_id = orders_products.order_id
                """
    rows = sql_read(sql)
    print("\n \tList of Orders: ")
    print(f"\t{'Id:' :<7} | {'Customer Name:' :<20} | {'Customer Address:' :<50} | {'Customer Phone:' :<20} | {'Courier Id:' :<15} | {'Order Status:' :<15} | {'Product Id:' :<10} | {'Quantity:' :<10} ")
    # for row in rows:
    #     print(f"\t{row[0] :<7} | {str(row[1]) :<20} | {row[2] :<50} | {row[3] :<20} | {row[4] :<15} | {row[5] :<15} | {row[6] :<10} | {row[7] :<10} ")

    for row in rows:
        print(f"\tId: {row[0]}, Customer Name: {str(row[1])}, Customer Address: {row[2]}, Customer Phone: {row[3]}, Courier: {row[4]}, Order Status: {row[5]}, Product: {row[6]}, Quantity: {row[7]}")






def order_id_check(details: str):
    
    while True:
        clear_screen()
        view_all_orders()
        id_choice = int_input_check(details)
        sql = "SELECT order_id FROM orders WHERE order_id=%s"
        data_check = sql_read(sql, id_choice)
        if not data_check:
            print(f"\n \Order with Id: {id_choice} doesn't exists. Please try again...")
            time.sleep(1)
            continue
        else:
            return id_choice

def view_all_order_statuses():
    
    sql = "SELECT status_id, order_status status FROM order_status"
    rows = sql_read(sql)
    print("\n \tList of order statuses: ")
    for row in rows:
        print(f"\tId: {row[0]}, Order Status: {row[1]}")

def order_status_check(details: str):
    
    while True:
        clear_screen()
        view_all_order_statuses()
        id_choice = int_input_check(details)
        sql = "SELECT status_id FROM order_status WHERE status_id=%s"
        data_check = sql_read(sql, id_choice)
        if not data_check:
            print(f"\n \tOrder status with Id: {id_choice} doesn't exists. Please try again...")
            time.sleep(1)
            continue
        else:
            return id_choice

def view_all_customers():
    
    sql = "SELECT customer_id, customer_name, customer_address, customer_phone FROM customers"
    rows = sql_read(sql)
    print("\n \tList of Customers: ")
    for row in rows:
        print(f"\tId: {row[0]}, Customer Name: {str(row[1])}, Customer Address: {row[2]}, Customer Phone: {row[3]}")

def customer_id_check(details: str):
    
    while True:
        clear_screen()
        view_all_customers()
        id_choice = int_input_check(details)
        sql = "SELECT customer_id FROM customers WHERE customer_id=%s"
        data_check = sql_read(sql, id_choice)
        if not data_check:
            print(f"\n \Customer with Id: {id_choice} doesn't exists. Please try again or ...")
            time.sleep(1)
            continue
        else:
            return id_choice

def customer_review():
    
    while True:
        clear_screen()
        view_all_customers()
        choice = input("\n \tWould you like to add a new customer [y / n] ").lower()
        if choice == 'y':
            customer_name = input("\tCustomer name: ")
            customer_address = input("\tCustomer address: ")
            customer_phone = input("\tCustomer phone number: ")
            
            order_dict = {'customer_name': customer_name, 
                    'customer_address': customer_address,
                    'customer_phone': customer_phone}
            sql = """INSERT INTO customers(customer_name, customer_address, customer_phone) 
                VALUES(%(customer_name)s, %(customer_address)s, %(customer_phone)s)"""
            sql_execute(sql, order_dict)
            sql = """SELECT customer_id FROM customers 
                WHERE customer_name=%(customer_name)s AND customer_address=%(customer_address)s AND customer_phone=%(customer_phone)s"""
            rows = sql_read(sql, order_dict)
            for row in rows:
                return row[0]
        elif choice == 'n':
            return customer_id_check("\n \tPlease use Id value of the customer you'd like to use? ")
        else:
            print("\n \tInvalid choice. Please try again...")

def order_items_review(order_id):

    task_check = True
    while task_check == True:
        clear_screen()
        view_all_products()
        product_id = product_id_check("\n \tPlease use Id value of the product you'd like to have in the order? ")
        quantity = product_stock_check(product_id, "\n \tHow many would you like to order? ")
        data = (order_id, product_id, quantity)
        sql = """INSERT INTO orders_products(order_id, product_id, quantity) 
                VALUES(%s, %s, %s)"""
        sql_execute(sql, data)

        task_check = task_choice("\n \tWould you like to add another product to this order? [y / n] ")
        
        
        
        
        
        
        
        
        
        
        
        
# def order_status_choice(details: str):
#     order_status_list = ['preparing', 'finalizing', 'completed', 'delivered', 'cancelled']
#     while True:
#         try:
#             clear_screen()
#             index_view(order_status_list)
#             idx_choice = int(input(details))
#             if idx_choice in range(len(order_status_list)):
#                 return idx_choice
#             else:
#                 raise ValueError
#         except ValueError:
#             print("")
#             print("\tInvalid choice. Please try again...")
#             time.sleep(0.5)

# def index_view(item_list):
#     print(f"""
#         Order status list:
#         ------------------------------------""")
#     for index, name in enumerate(item_list):
#         print(f"\t[{index}] - {name}")
#     print("")


# def does_index_exist(products_list, o_items):
#     for idx in o_items:
#         try:
#             products_list[idx]
#         except (IndexError, ValueError):
#             return False
#     return True

# def user_idx_choice(item_name, item_list, task):
#     while True:
#         try:
#             clear_screen()
#             index_view(item_name, item_list)
#             idx_choice = int(input(f"\tPlease use index value for {item_name} details to be {task}. "))
#             if idx_choice in range(len(item_list)):
#                 return idx_choice
#             else:
#                 raise ValueError
#         except ValueError:
#             print("")
#             print("\tInvalid choice. Please try again...")
#             time.sleep(0.5)

# def end_of_task_choice(item_name, task):
#     while True:
#         clear_screen()
#         print("")
#         user_choice = input(f"\tWould you like to {task} another {item_name}? [y / n] ")
#         if user_choice == 'y':
#             return True
#         elif user_choice == 'n':
#             return False
#         else:
#             print("")
#             print("\tInvalid choice. Please try again...")





# #Product, Courier & Order Deletion Function - COMPLETE
# def item_del(item_name: str, item_list: List):
    
#     check = True
#     while check == True:
#         idx_choice = user_idx_choice(item_name, item_list, 'deleted')
#         while True:
#             clear_screen()
#             user_choice = input(f"\tAre you sure you want to remove {item_list[idx_choice]} ( y / n ): ").lower()                
#             if user_choice == 'y':
#                 print(f"\n {item_list[idx_choice]} has been removed.")
#                 item_list.pop(idx_choice)
#                 time.sleep(1)
#                 break
#             elif user_choice == 'n':
#                 print(f"\n No {item_name}s has been deleted")
#                 time.sleep(1)
#                 break
#             else:
#                 print("\tInvalid choice. Please try again...")
#         check = end_of_task_choice(item_name, 'delete')