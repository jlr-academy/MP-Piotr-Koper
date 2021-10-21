import os
import time
import pymysql
from dotenv import load_dotenv
from typing import List, Dict
from file_handler import load_data, save_data
from utils import index_view, user_idx_choice, end_of_task_choice, clear_screen
from product_mgmt import product_menu
from courier_mgmt import courier_menu
from order_mgmt import orders_menu

# products = [Product(1, 'Tea', 1.0, 20),Product(1, 'Plum', 5.0, 100)]

# Main Function
def main():
    
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
    
    products_list = load_data('products')
    couriers_list = load_data('couriers')
    orders_list = load_data('orders')
    order_status_list = ['preparing', 'finalizing', 'completed']

    main_menu(products_list, couriers_list, orders_list, order_status_list, connection, cursor)

#Main Menu Function - COMPLETE
def main_menu(products_list: List, couriers_list: List, orders_list: List, order_status_list: List, connection, cursor):

    mm_choice = ""
    while mm_choice != 0:
        clear_screen()
        print("""
        Main Menu:
        -------------------
        [0]. Exit App
        [1]. Product Menu
        [2]. Courier Menu
        [3]. Order Menu""")
        mm_choice = input("\tPlease pick a menu option: ")
        if mm_choice == '0':
            save_and_exit(products_list, couriers_list, orders_list)                        
        elif mm_choice == '1':
            product_menu(connection, cursor)
        elif mm_choice == '2':
            courier_menu(connection, cursor)
        elif mm_choice == '3':
            orders_menu(products_list, couriers_list, orders_list, order_status_list)
        else:
            print("\n \tInvalid choice. Please try again...")

#App Exit and Save Files Function - COMPLETE
def save_and_exit(products_list: List, couriers_list: List, orders_list: List, connection, cursor):
    
    save_data('products', products_list)
    save_data('couriers', couriers_list)
    save_data('orders', orders_list)
    
    # Closes the cursor so will be unusable from this point 
    cursor.close()

    # Closes the connection to the DB, make sure you ALWAYS do this
    connection.close()

    
    print("""
    \tAll files updated and saved.
    \tApp is closing....""")
    
    time.sleep(1)
    exit()

#List View Function - REDUNDANT
def list_view(item_name: str, item_list: List):
    
    clear_screen()
    index_view(item_name, item_list)
    os.system('pause')

#Adding new Product & Courier Fuction - REDUNDANT
def add_new_item(item_name: str, item_list: List):
    
    clear_screen()
    if item_name == 'product':
        while True:
            p_name = input(f"\tWhat is the new {item_name} name? ").lower().title()  
            if item_list == [] or not any(product_dic["name"] == p_name for product_dic in item_list):
                p_price = float(input(f"\tWhat is the {p_name} price? "))
                product_dic = {
                    "name": p_name,
                    "price": p_price   
                }
                print(f"\t{product_dic} has been created")
                time.sleep(1)
                item_list.append(product_dic)
                break
            else:
                print(f"\t {p_name} already exists. Please try again...")
                time.sleep(0.5)
    elif item_name == 'courier':
        while True:
            c_name = input(f"\tWhat is the new {item_name} name? ").lower().title()
            if item_list == [] or not any(courier_dic["name"] == c_name for courier_dic in item_list):
                c_phone = input(f"\tWhat is the {c_name} phone number? ")
                courier_dic = {
                    "name": c_name,
                    "phone": c_phone   
                }
                print(f"\t{courier_dic} has been created")
                time.sleep(1)
                item_list.append(courier_dic)
                break
            else:
                print(f"\t {c_name} already exists. Please try again...")
                time.sleep(0.5)

#Updating Products & Couriers Function - COMPLETE
def item_updt(item_name: str, item_list: List):

    check = True
    while check == True:
        idx_choice = user_idx_choice(item_name, item_list, 'updated')
        while True:
            try:
                clear_screen()
                item_dict: Dict = item_list[idx_choice]
                print(f"\t{item_dict} details:")                   
                for index, (key, value) in enumerate(item_dict.items()):
                    print(f"\t[{index}] - {key} - {value}")
                keys = list(item_dict)
                dict_choice = int(input("\tWhich element would you like to update? Use index value. "))
                if dict_choice in range(len(list(item_dict))):
                    value = input(f"\tWhat is the new {keys[dict_choice]}: ")
                    if value != "":
                        item_dict.update({keys[dict_choice] : value})
                        print(f"\t{keys[dict_choice].title()} has been updated")
                        time.sleep(0.5)
                        break
                    else:
                        pass
                else:
                    raise ValueError
            except  ValueError:
                print("\tInvalid choice. Please try again...")
                time.sleep(0.5)
        check = end_of_task_choice(item_name, 'update')


#Trying to implement Class functionality for products

# def create_new_product():

#     clear_screen()
#     product = Product(id = '0', #generated via database
#                     name = name_duplication(),
#                     price = float_input(),
#                     qty = int_input)
#     products.append(product)
#     print(products)
#     os.system('pause')
#     return products

# def name_duplication():
#     while True:
#         name = upper_case_conversion(input("\tWhat is the new product name? "))
#         if products == [] or not any(name == i.name for i in products):
#             return name
#         else:
#             print(f"\tProduct already exists. Please try again...")
#             time.sleep(0.5)
#             continue

# def float_input():
#     while True:
#         try:
#             price = float(input("\tWhat is the product price? "))
#             return price
#         except ValueError:
#             print("\tInvalid input. Please try again...")

# def int_input():
#     while True:
#         try:
#             qty = int(input("\tWhat is the product price? "))
#             return qty
#         except ValueError:
#             print("\tInvalid input. Please try again...")


if __name__ == "__main__":
    main()
    
