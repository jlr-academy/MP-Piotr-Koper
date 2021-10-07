import os
import time
from typing import List
from homefh import load_data, save_data

# Main Function
def main():
    
    products_list = load_data('products')
    couriers_list = load_data('couriers')
    orders_list = load_data('orders')

    main_menu(products_list, couriers_list, orders_list)

#Main Menu Function
def main_menu(products_list: List, couriers_list: List, orders_list: List):
    
    while True:
        try:
            os.system('CLS')
            mm_options = int(input("""
                            Main Menu:
                            -------------------
                            0. Exit App
                            1. Product Menu
                            2. Courier Menu
                            3. Order Menu
                            
                            Please pick a menu option: """))
            if mm_options in [0,1,2,3]:
                if mm_options == 0:
                    save_and_exit()                        
                elif mm_options == 1:
                    sub_menu("product", products_list)
                elif mm_options == 2:
                    sub_menu("courier", couriers_list)
                elif mm_options == 3:
                    orders_menu(orders_list, couriers_list)
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
                            ----------------------------
                            0. Return to Main Menu
                            1. Print {item_name}s list
                            2. Create a new {item_name}
                            3. Update {item_name} details
                            4. Delete {item_name}
                            
                            Please pick a menu option: """))
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
def orders_menu(orders_list: List, couriers_list: List):

    while True:
        try:
            os.system('CLS')
            om_options = int(input(f"""
                            Orders Menu:
                            -------------------------
                            0. Return to Main Menu
                            1. Print orders list
                            2. Create a new order
                            3. Update order status
                            4. Update existing order
                            5. Delete order
                            
                            Please pick a menu option: """))
            if om_options in [0,1,2,3,4,5]:
                if om_options == 0:
                    break
                elif om_options == 1:
                    list_view('order', orders_list)
                elif om_options == 2:
                    new_order(orders_list, couriers_list)
                elif om_options == 3:
                    ord_status_updt('order', orders_list)
                elif om_options == 4:
                    order_updt('order', orders_list)
                elif om_options == 5:
                    order_del('order', orders_list)
            else:
                raise ValueError 
        except (TypeError, ValueError):
            print("\n Wrong option selected, please try again..")
            time.sleep(0.5)

#App Exit and save files Function
def save_and_exit(products_list: List, couriers_list: List, orders_list: List):
    
    save_data('products', products_list)
    save_data('couriers', couriers_list)
    save_data('orders', orders_list)
    os.system('CLS')
    print("""   
                All files updated and saved.
                
                App is closing....""")
    time.sleep(1)
    exit()

#List View Function
def list_view(item_name: str, item_list: List):
    os.system('CLS')
    print(f"\n {item_name.title()} list:")
    print("-----------------")
    for index, name in enumerate(item_list):
        print(f"[{index}] - {name}")
    input("\n Press 'Enter' to continue...")

#Adding Fuction
def new_item(item_name, item_list: List):
    
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

def new_order(orders_list: List, couriers_list: List):
    
    os.system('CLS')
    order_dic = {}
    print("\n Please provide following new order details:")
    order_dic["customer_name"] = input("\n Customer name: ")
    order_dic["customer_address"] = input("\n Customer address: ")
    order_dic["customer_phone"] = int(input("\n Customer phone number: "))
    list_view('courier', couriers_list)
    order_dic["courier"] = int(input("\n Pick courier to be assign to this order. Use index value: "))
    order_dic["status"] = "preparing" 
    print("\n Order logged and status updated to preparing...")
    time.sleep(2)    
    orders_list.append(order_dic)

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

if __name__ == "__main__":
    main()