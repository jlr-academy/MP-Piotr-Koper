import os
import time
from typing import List

def float_input_check(details: str):
    if details == "":
        return ""
    else:
        while True:
            try:
                clear_screen()
                price = float(input(details))
                return price
            except ValueError:
                print("\n \tInvalid input. Please try again...")

def int_input_check(details: str):
    
    while True:
        try:
            integer = int(input(details))
            return integer
        except ValueError:
            print("\n \tInvalid input. Please try again...")

def products_view_all(cursor):
    
    cursor.execute("SELECT product_id, name, price FROM products")
    rows = cursor.fetchall()
    for row in rows:
        print(f'\tId: {row[0]}, Name: {str(row[1])}, Price: {row[2]}')

def couriers_view_all(cursor):
    
    cursor.execute("SELECT courier_id, name, phone FROM couriers")
    rows = cursor.fetchall()
    for row in rows:
        print(f'\tId: {row[0]}, Name: {str(row[1])}, Phone: {row[2]}')

def product_name_duplicate_check(cursor, details: str):
    
    while True:
        name = upper_case_conversion(input(details))
        cursor.execute("SELECT name FROM products WHERE name=%s",(name))
        data_check = cursor.fetchall()
        if not data_check:
            return name
        else:
            print(f"\n \t{name} already exists. Please try again...")

        
def product_id_check(cursor, details: str):
    
    while True:
        id_choice = int_input_check(details)
        cursor.execute("SELECT product_id FROM products WHERE product_id=%s",(id_choice))
        data_check = cursor.fetchall()
        if not data_check:
            print(f"\n \tProduct with Id: {id_choice} doesn't exists. Please try again...")
            continue
        else:
            return id_choice

def courier_id_check(cursor, details: str):
    
    while True:
        id_choice = int_input_check(details)
        cursor.execute("SELECT courier_id FROM couriers WHERE courier_id=%s",(id_choice))
        data_check = cursor.fetchall()
        if not data_check:
            print(f"\n \tCourier with Id: {id_choice} doesn't exists. Please try again...")
        else:
            return id_choice

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
        clear_screen()
        print("")
        user_choice = input(details.lower())
        if user_choice == 'y':
            return True
        elif user_choice == 'n':
            return False
        else:
            print("")
            print("\tInvalid choice. Please try again...")



















def index_view(item_name, item_list):
    print(f"""
        {item_name.title()} list:
        ------------------------------------""")
    for index, name in enumerate(item_list):
        print(f"\t[{index}] - {name}")
    print("")

def does_index_exist(products_list, o_items):
    for idx in o_items:
        try:
            products_list[idx]
        except (IndexError, ValueError):
            return False
    return True

def user_idx_choice(item_name, item_list, task):
    while True:
        try:
            clear_screen()
            index_view(item_name, item_list)
            idx_choice = int(input(f"\tPlease use index value for {item_name} details to be {task}. "))
            if idx_choice in range(len(item_list)):
                return idx_choice
            else:
                raise ValueError
        except ValueError:
            print("")
            print("\tInvalid choice. Please try again...")
            time.sleep(0.5)

def end_of_task_choice(item_name, task):
    while True:
        clear_screen()
        print("")
        user_choice = input(f"\tWould you like to {task} another {item_name}? [y / n] ")
        if user_choice == 'y':
            return True
        elif user_choice == 'n':
            return False
        else:
            print("")
            print("\tInvalid choice. Please try again...")

def clear_screen():
    # Clearing screen is different depending on whether windows or unix-like
    os.system('cls' if os.name == 'nt' else 'clear')



#Product, Courier & Order Deletion Function - COMPLETE
def item_del(item_name: str, item_list: List):
    
    check = True
    while check == True:
        idx_choice = user_idx_choice(item_name, item_list, 'deleted')
        while True:
            clear_screen()
            user_choice = input(f"\tAre you sure you want to remove {item_list[idx_choice]} ( y / n ): ").lower()                
            if user_choice == 'y':
                print(f"\n {item_list[idx_choice]} has been removed.")
                item_list.pop(idx_choice)
                time.sleep(1)
                break
            elif user_choice == 'n':
                print(f"\n No {item_name}s has been deleted")
                time.sleep(1)
                break
            else:
                print("\tInvalid choice. Please try again...")
        check = end_of_task_choice(item_name, 'delete')