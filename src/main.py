
import os
import time
from typing import List
from file_handler import load_data, save_data 

products_list = []
couriers_list = []
orders_list = []
orders_status_list = ['preparing', 'finalizing', 'completed']
load_data(products_list, couriers_list, orders_list)

#Main Menu Function
def main_menu():
    while True:
        try:
            os.system('CLS')
            mm_options = int(input("""
                            0. Exit App
                            1. Product Menu
                            2. Courier Menu
                            3. Order Menu
                            
                            Please pick required menu option: """))
            if mm_options in [0,1,2,3]:
                if mm_options == 0:
                    save_and_exit()                        
                elif mm_options == 1:
                    sub_menu("product", products_list)
                elif mm_options == 2:
                    sub_menu("courier", couriers_list)
                elif mm_options == 3:
                    orders_menu()
            else:
                raise ValueError 
        except (TypeError, ValueError):
            print("\n Wrong option selected, please try again..")
            time.sleep(0.5)

#Sub Menu Function
def sub_menu(item_name: str, item_list: List):
    while True:
        try:
            os.system('CLS')
            sm_options = int(input(f"""
                            {item_name.title()} Menu:
                            0. Return to Main Menu
                            1. Print {item_name}s list
                            2. Create a new {item_name}
                            3. Update {item_name} details
                            4. Delete {item_name}
                            
                            Please pick required menu option: """))
            if sm_options in [0,1,2,3,4]:
                if sm_options == 0:
                    break
                elif sm_options == 1:
                    list_view(item_name, item_list)
                elif sm_options == 2:
                    new_item(item_name, item_list)
                elif sm_options == 3:
                    item_updt(item_name, item_list)
                elif sm_options == 4:
                    item_del(item_name, item_list)
            else:
                raise ValueError 
        except (TypeError, ValueError):
            print("\n Wrong option selected, please try again..")
            time.sleep(0.5)

#Order Menu Function
def orders_menu():
    while True:
        try:
            os.system('CLS')
            om_options = int(input(f"""
                                Orders Menu:
                            0. Return to Main Menu
                            1. Print orders list
                            2. Create a new order
                            3. Update order status
                            4. Update existing order
                            5. Delete order
                            
                            Please pick required menu option: """))
            if om_options in [0,1,2,3,4,5]:
                if om_options == 0:
                    break
                elif om_options == 1:
                    list_view('order', orders_list)
                elif om_options == 2:
                    new_item('order', orders_list)
                elif om_options == 3:
                    item_updt('order', orders_list)
                elif om_options == 4:
                    order_updt('order', orders_list)
                elif om_options == 5:
                    item_del('order', orders_list)
            else:
                raise ValueError 
        except (TypeError, ValueError):
            print("\n Wrong option selected, please try again..")
            time.sleep(0.5)



#App Exit and save files Function
def save_and_exit():
    save_data(products_list, couriers_list, orders_list)
    os.system('CLS')
    print("""   
                All files updated and saved.
                
                App is closing....""")
    time.sleep(1)
    exit()

#List View Function
def list_view(item_name, item_list):
    os.system('CLS')
    print(f"\n {item_name.title()} list:")
    print("-----------------")
    for i in range(len(item_list)):
                print(f"[{i}] - {item_list[i]}")
    input("\n Press 'Enter' to continue...")

#Adding Fuction
def new_item(item_name, item_list: List):
    if item_name == 'order':
        os.system('CLS')
        order_dic = {}
        print("\n Please provide following details for the new order :")
        order_dic["customer_name"] = input("\n Customer name: ")
        order_dic["customer_address"] = input("\n Customer address: ")
        order_dic["customer_phone"] = int(input("\n Customer phone number: "))
        for i in range(len(couriers_list)):
                    print(f"[{i}] - {couriers_list[i]}")
        order_dic["courier"] = int(input("\n Pick courier to be assign to this order. Use index value: "))
        order_dic["status"] = "preparing" 
        print("\n Order logged and status updated to preparing...")
        time.sleep(2)    
        orders_list.append(order_dic)
    else:    
        while True:
            os.system('CLS')
            x = input(f"\n What is the name of the new {item_name}? ").lower().title()
            if x in item_list:
                print(f"\n {x} already exists. Please try again...")
                time.sleep(1)
            else:
                item_list.append(x) 
                print(f"\n {x} has been added.")
                print(f"\n New {item_name} list: {item_list}")
                menu_dec(item_name, item_list)
                break
            
#Updating Function
def item_updt(item_name, item_list):
    while True:
        try:
            os.system('CLS')
            for i in range(len(item_list)):
                print(f" Index [{i}] - {item_list[i]}")
            x = int(input(f"\n Which {item_name} would you like to update? Use {item_name} index value. "))
            if x in range(len(item_list)):
                if item_name == 'order':
                    for i in range(len(orders_status_list)):
                        print(f" Index [{i}] - {orders_status_list[i]}")
                    z =  int(input(f"\n What is the new order status? Use index value. "))
                    order_dic = item_list[x]
                    order_dic["status"] = orders_status_list[z]
                    print(f"\n Order status has been updated to {orders_status_list[z]}")
                    menu_dec(item_name, item_list)
                    break
                else:    
                    while True:
                        y = input(f"\n What is the new {item_name} name? ").lower().title()      
                        if y in item_list:
                            print(f"\n {y} already exists.Please try again... ")
                        else:
                            os.system('CLS')
                            print(f"\n {item_list[x]} has been updated to {y} ")
                            item_list[x] = y
                            print(f"\n New {item_name} list: \n")
                            for i in range(len(item_list)):
                                print(f" Index [{i}] - {item_list[i]}")
                            menu_dec(item_name, item_list)
                            break
            else:
                raise ValueError
        except (TypeError, ValueError):
            print("\n Selected option doesn't meet required criteria, please try again..")
            time.sleep(0.5)

#Removing Function
def item_del(item_name, item_list):
    if item_name == 'order':
        for i in range(len(item_list)):
            print(f" Index [{i}] - {item_list[i]}")
        del_choice = int(input(f"\n Which {item_name} would you like to delete? Use {item_name} index value."))
        item_list.pop(del_choice)
    else:
        while True:
            os.system('CLS')
            print(f"\n {item_list}")
            z = input(f"\n Which {item_name} would you like to delete? ").lower().title()
            if z not in item_list:
                print(f"\n Chosen {item_name} not in the {item_list} list. Please try again...")
                time.sleep(0.5)
            else:
                decision = input(f"\n Are you sure you want to remove {z} ( y / n ): ")
                if decision == 'y':
                    item_list.remove(z)
                    print(f"\n {z} has been removed.")
                    new_list = item_list
                    print(f"\n New {item_name} list: {new_list}")
                    menu_dec(item_name, item_list)
                    break
                else:
                    menu_dec(item_name, item_list)
                    break

#Menu User Decison Fuction
def menu_dec(item_name: str, item_list: List):
    m_choice = input(f"\n Would you like to come back to the '{item_name.title()} menu'? (y/n) ").lower()
    if (m_choice != 'y' and m_choice != 'n'):
        print("\n Wrong option selected, please try again..")
        time.sleep(0.5)
        menu_dec(item_name, item_list)
    else:
        if m_choice == 'y':
            return
        else:
            main_menu()

def order_updt(item_name, item_list):
    os.system('CLS')
    for i in range(len(item_list)):
        print(f" Index [{i}] - {item_list[i]}")
    x = int(input(f"\n Which {item_name} would you like to update? Use {item_name} index value. "))
    order_dic = item_list[x]
    for key, value in order_dic.items():
        if key == "courier":
            for index, name in enumerate(couriers_list):
                print(f"[{index}] - {name}")
            value = input("\n Pick new courier to be assign to this order. Use index value: ")
            if value != "":
                order_dic.update({key : int(value)})
            else:
                continue
        elif key == "status":
            for index, name in enumerate(orders_status_list):
                print(f"[{index}] - {name}")
            index_choice = input(f"\n What is the new order status? Use index value. ")
            if index_choice != "":
                value = orders_status_list[int(index_choice)]
                order_dic.update({key : value})
            else:
                continue
        else:
            value = input(f"What is the new {key}: ")
            if value != "":
                order_dic.update({key : value})
            else:
                continue
main_menu()

