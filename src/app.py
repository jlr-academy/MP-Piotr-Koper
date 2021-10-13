import os
import time
from typing import List, Dict
from file_handler import load_data, save_data
from utils import index_view, does_index_exist

# Main Function
def main():
    
    products_list = load_data('products')
    couriers_list = load_data('couriers')
    orders_list = load_data('orders')
    order_status_list = ['preparing', 'finalizing', 'completed']

    main_menu(products_list, couriers_list, orders_list, order_status_list)

#Main Menu Function - COMPLETE
def main_menu(products_list: List, couriers_list: List, orders_list: List, order_status_list: List):
    
    mm_choice = ""
    while mm_choice != 0:
        os.system('CLS')
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
            pc_menu("product", products_list)
        elif mm_choice == '2':
            pc_menu("courier", couriers_list)
        elif mm_choice == '3':
            orders_menu(products_list, couriers_list, orders_list, order_status_list)
        else:
            print("Invalid choice. Please try again...")

#Products & Couriers Menu Function - COMPLETE
def pc_menu(item_name: str, item_list: List):

    pcm_choice = ""
    while pcm_choice != 0:
        os.system('CLS')
        print(f"""
        {item_name.title()} Menu:
        ------------------------------
        [0]. Return to Main Menu
        [1]. View {item_name}s list
        [2]. Create a new {item_name}
        [3]. Update {item_name} details
        [4]. Delete {item_name}""")
        pcm_choice = input("\tPlease pick a menu option: ")
        if pcm_choice == '0':
            break
        elif pcm_choice == '1':
            list_view(item_name, item_list)
        elif pcm_choice == '2':
            add_new_item(item_name, item_list)
        elif pcm_choice == '3':
            item_updt(item_name, item_list)
        elif pcm_choice == '4':
            item_del(item_name, item_list)
        else:
            print("Invalid choice. Please try again...")

#Order Menu Function - COMPLETE
def orders_menu(products_list: List, couriers_list: List, orders_list: List, order_status_list: List, ):

    om_choice = []
    while om_choice != 0:
        os.system('CLS')
        print("""
        Orders Menu:
        ------------------------------
        [0]. Return to Main Menu
        [1]. View orders list
        [2]. Create a new order
        [3]. Update order status
        [4]. Update existing order
        [5]. Delete order""")
        om_choice = input("\tPlease pick a menu option: ")
        if om_choice == '0':
            break
        elif om_choice == '1':
            list_view('order', orders_list)
        elif om_choice == '2':
            add_new_order(products_list, couriers_list, orders_list)
        elif om_choice == '3':
            order_status_updt(orders_list, order_status_list)
        elif om_choice == '4':
            order_updt(products_list, couriers_list, orders_list, order_status_list)
        elif om_choice == '5':
            item_del('order', orders_list)
        else:
            print("Invalid choice. Please try again...")

#App Exit and Save Files Function - COMPLETE
def save_and_exit(products_list: List, couriers_list: List, orders_list: List):
    
    save_data('products', products_list)
    save_data('couriers', couriers_list)
    save_data('orders', orders_list)
    
    print("""
    \tAll files updated and saved.
    \tApp is closing....""")
    
    time.sleep(1)
    exit()

#List View Function - COMPLETE
def list_view(item_name: str, item_list: List):
    
    os.system('cls')
    index_view(item_name, item_list)
    os.system('pause')

#Adding new Product & Courier Fuction - COMPLETE
def add_new_item(item_name: str, item_list: List):
    
    os.system('cls')
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
                c_price = input(f"\tWhat is the {c_name} phone number? ")
                courier_dic = {
                    "name": c_name,
                    "phone": c_price   
                }
                print(f"\t{courier_dic} has been created")
                time.sleep(1)
                item_list.append(courier_dic)
                break
            else:
                print(f"\t {c_name} already exists. Please try again...")
                time.sleep(0.5)

#Adding new Order Function - COMPLETE
def add_new_order(products_list: List, couriers_list: List, orders_list: List):
    
    os.system('CLS')
    print("\tPlease provide new order details:")
    o_customer_name = input("\tCustomer name: ")
    o_customer_address = input("\tCustomer address: ")
    o_customer_phone = input("\tCustomer phone number: ")
    while True:
        try:
            os.system('cls')
            index_view('courier', couriers_list)
            o_courier = int(input("\tPick courier to be assign to this order. Use index value: "))
            if o_courier in range(len(couriers_list)):
                o_status = "preparing" 
                while True:
                    try:
                        os.system('cls')
                        index_view('product', products_list)
                        o_items = [int(x) for x in input("\tPick products to be added to this order. Use index value and separate with comma: ").split(',')]
                        if does_index_exist(products_list, o_items) is True:
                            order_dic = {
                                "customer_name": o_customer_name,
                                "customer_address": o_customer_address,
                                "customer_phone": o_customer_phone,
                                "courier": o_courier,
                                "status": o_status,
                                "items": o_items
                            }
                            orders_list.append(order_dic)
                            print("\tOrder logged and status set to 'PREPARIG'...")
                            time.sleep(2)
                            break
                        else:
                            print("\tSelected products out of range. Please try again...")
                            time.sleep(0.5)  
                    except ValueError:
                        print("\tInvalid choice. Please try again...")
                        time.sleep(0.5)
                break         
            else:
                raise ValueError
        except ValueError:
            print("\tInvalid choice. Please try again...")
            time.sleep(0.5) 
    
#Updating Products & Couriers Function - COMPLETE
def item_updt(item_name: str, item_list: List):

    while True:
        try:
            os.system('cls')
            index_view(item_name, item_list)
            x = int(input(f"\n Which {item_name} would you like to update? Use {item_name} index value. "))
            if x in range(len(item_list)):
                while True:
                    try:
                        os.system('cls')
                        item_dict: Dict = item_list[x]                   
                        for index, (key, value) in enumerate(item_dict.items()):
                            print(f"[{index}] - {key} - {value}")
                        keys = list(item_dict)
                        dict_choice = int(input("\n Which element would you like to update? Use index value. "))
                        if dict_choice in range(len(list(item_dict))):
                            value = input(f" What is the new {keys[dict_choice]}: ")
                            if value != "":
                                item_dict.update({keys[dict_choice] : value})
                                print(f"{keys[dict_choice].title()} has been updated")
                                time.sleep(0.5)
                                break
                            else:
                                pass
                        else:
                            raise ValueError
                    except  ValueError:
                        print(" Invalid choice. Please try again...")
                        time.sleep(0.5)
                os.system('cls')
                decision = input(f" Would you like to update another {item_name}? (y / n) ")
                if decision == 'y':
                    pass
                else:
                    break
            else:
                raise ValueError     
        except ValueError:
            print(" Invalid choice. Please try again...")
            time.sleep(0.5)
        
#Updating Order Status Function - COMPLETE
def order_status_updt(orders_list: List, order_status_list: List):
    while True:
        try:
            os.system('cls')
            index_view('order', orders_list)
            x = int(input(f"\n Which order status would you like to update? Use order index value. "))
            if x in range(len(orders_list)):
                while True:
                    try:
                        os.system('cls')
                        index_view('order status', order_status_list )
                        z =  int(input(f"\n Please use index value to assign new order status. "))
                        if z in range(len(order_status_list)):
                            order_dic = orders_list[x]
                            order_dic["status"] = order_status_list[z]
                            print(f"\n Order status has been updated to {order_status_list[z]}")
                            time.sleep(0.5)
                            break
                        else:
                            raise ValueError
                    except ValueError:
                        print(" Invalid choice. Please try again...")
                        time.sleep(0.5)
                os.system('cls')
                decision = input(" Would you like to update another order status? (y / n) ")
                if decision == 'y':
                    pass
                else:
                    break
            else:
                raise ValueError
        except ValueError:
            print(" Invalid choice. Please try again...")
            time.sleep(0.5)

#Updating Order Details Function - TBC
def order_updt(products_list: List, couriers_list: List, orders_list: List, order_status_list: List):
    while True:
        try:
            os.system('cls')
            index_view('order', orders_list)
            x = int(input(f"\tWhich order would you like to update? Use order index value. "))
            if x in range(len(orders_list)):
                while True:
                    os.system('cls')
                    order_dict: Dict = orders_list[x]
                    for index, (key, value) in enumerate(order_dict.items()):
                        print(f"[{index}] - {key} - {value}")
                    keys = list(order_dict)
                    dict_choice = int(input("\tWhich element would you like to update? Use index value. "))
                    if keys[dict_choice] == 'courier':
                        index_view('courier', couriers_list)
                        value = input("\tPick new courier to be assign to this order. Use index value: ")
                        if value != "":
                            order_dict.update({keys[dict_choice] : int(value)})
                        else:
                            pass
                    elif keys[dict_choice] == 'status':
                        index_view('status', order_status_list)
                        index_choice = input(f"\tWhat is the new order status? Use index value. ")
                        if index_choice != "":
                            value = order_status_list[int(index_choice)]
                            order_dict.update({keys[dict_choice] : value})
                        else:
                            pass
                    elif keys[dict_choice] == 'items':
                        while True:
                            try:
                                index_view('product',products_list)
                                o_items: List = [int(x) for x in input("\tPick products to be added / updated for this order. Use index value and separate with comma: ").split(',')]
                                if o_items != "":
                                    if does_index_exist(products_list, o_items) is True:
                                        order_dict.update({keys[dict_choice] : o_items})
                                        break
                                    else:
                                        print("\tSelected products out of range. Please try again...")
                                        time.sleep(0.5)
                                else:
                                    pass
                            except ValueError:
                                print(" Invalid choice. Please try again...")
                    else:
                        value = input(f"\tWhat is the new {keys[dict_choice]}: ")
                        if value != "":
                            order_dict.update({keys[dict_choice] : value})
                        else:
                            pass
                    decision = input("\tWould you like to change another element? (y / n) ")
                    if decision == 'y':
                        pass
                    else:
                        break            
            else:
                raise ValueError                
        except (TypeError, ValueError):
            print(" Invalid choice. Please try again...")
            time.sleep(0.5)

#Product, Courier & Order Deletion Function - COMPLETE
def item_del(item_name: str, item_list: List):
    while True:
        try:
            os.system('cls')
            index_view(item_name, item_list)
            user_choice = int(input(f"\n Which {item_name} would you like to delete? Use {item_name} index value. "))
            if user_choice in range(len(item_list)):
                while True:
                    os.system('cls')
                    decision = input(f"\n Are you sure you want to remove {item_list[user_choice]} ( y / n ): ").lower()                
                    if decision not in ['y','n']:
                        print("\n Wrong option selected, please try again..")
                    elif decision == 'y':
                        print(f"\n {item_list[user_choice]} has been removed.")
                        item_list.pop(user_choice)
                        time.sleep(1)
                        break
                    else:
                        print(f"\n No {item_name}s has been deleted")
                        time.sleep(1)
                        break
                decision = input(f" Would you like to delete another {item_name}? (y / n) ")
                if decision == 'y':
                    pass
                else:
                    break
            else:
                raise ValueError
        except (TypeError, ValueError):
            print(" Invalid choice. Please try again...")
            time.sleep(0.5) 
            
if __name__ == "__main__":
    main()