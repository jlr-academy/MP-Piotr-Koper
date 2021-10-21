import os
import time
from typing import List, Dict
from utils import index_view, end_of_task_choice
from utils import user_idx_choice, does_index_exist, item_del
from utils import clear_screen

#Order Menu Function - COMPLETE
def orders_menu(products_list: List, couriers_list: List, orders_list: List, order_status_list: List):
    om_choice = []
    while om_choice != 0:
        clear_screen()
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
            orders_view(orders_list)
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
            
#Print all orders by defoult, courier or list
#To improve User interaction
def orders_view(orders_list):
    while True:
        try:
            os.system('cls')
            print("""
        Please select the way you'd like to preview orders [ sorted by ]:
        [1]. Default
        [2]. Status 
        [3]. Courier""")
            choice = input("\t")
            if choice =='1':
                index_view('orders', orders_list)
                os.system('pause')
                break
            elif choice == '2':
                sorted(orders_list, key=lambda x: x.get('status'))
                index_view('orders', orders_list)
                os.system('pause')
                break
            elif choice == '3':
                sorted(orders_list, key=lambda x: x.get('courier'))
                index_view('orders', orders_list)
                os.system('pause')
                break
            else:
                raise ValueError
        except ValueError:
            print("")
            print("\tInvalid choice. Please try again...")
            time.sleep(0.5)
        
#Adding new Order Function - COMPLETE
def add_new_order(products_list: List, couriers_list: List, orders_list: List):
    check = True
    while check == True:
        os.system('CLS')
        print("\tPlease provide new order details:")
        o_customer_name = input("\tCustomer name: ")
        o_customer_address = input("\tCustomer address: ")
        o_customer_phone = input("\tCustomer phone number: ")
        o_courier = str(user_idx_choice('courier', couriers_list, 'assigned'))
        o_status = "preparing"
        o_items =  add_items_to_order(products_list, 'added')
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
        check = end_of_task_choice('order', 'add')

#Checking if products exist in product_list and if yes add them to the order        
def add_items_to_order(products_list, task):
    while True:
        try:
            os.system('cls')
            index_view('product', products_list)
            o_items = [int(x) for x in input(f"\tPlease use index value separated with comma for product(s) to be {task} to this order. ").split(',')]
            if does_index_exist(products_list, o_items) is True:
                return o_items
            else:
                print("")
                print("\tSelected products out of range. Please try again...")
                time.sleep(0.5)  
        except ValueError:
            print("")
            print("\tInvalid choice. Please try again...")
            time.sleep(0.5)

#Updating Order Status Function - COMPLETE
def order_status_updt(orders_list: List, order_status_list: List):
    check = True
    while check == True:
        o_idx_choice = user_idx_choice('order', orders_list, 'updated')
        os_idx_choice = user_idx_choice('order status', order_status_list, 'updated')
        order_dic = orders_list[o_idx_choice]
        order_dic["status"] = order_status_list[os_idx_choice]
        print(f"\tOrder status has been updated to {order_status_list[os_idx_choice]}")
        time.sleep(0.5)
        check = end_of_task_choice('order status', 'update')

#Updating Order Details Function - COMPLETE
def order_updt(products_list: List, couriers_list: List, orders_list: List, order_status_list: List):
    while True:
        o_idx_choice = user_idx_choice('order', orders_list, 'updated')
        while True:
            try:
                os.system('cls')
                order_dict: Dict = orders_list[o_idx_choice]
                print(f"\tCustomer order details:")
                for index, (key, value) in enumerate(order_dict.items()):
                    print(f"\t[{index}] - {key} - {value}")
                keys = list(order_dict)
                dict_choice = int(input("\tPlease use index value for order element to be update: "))
                if keys[dict_choice] == 'courier':
                    while True:
                        try:
                            os.system('cls')
                            index_view('courier', couriers_list)
                            value = input("\tPlease use index value for new courier to be assigned: ")
                            if value == "":
                                break
                            elif int(value) not in range(len(couriers_list)):
                                raise ValueError
                            else:    
                                order_dict.update({keys[dict_choice] : int(value)})
                                print(f"\tCourier updated to {value}: {couriers_list[int(value)]}")
                                break
                        except ValueError:
                            print("\tInvalid choice. Please try again...")
                elif keys[dict_choice] == 'status':
                    while True:
                        try:
                            os.system('cls')
                            index_view('status', order_status_list)
                            index_choice = input(f"\tPlease use index value for new order status to be assigned: ")
                            if index_choice == "":
                                break
                            elif int(index_choice) not in range(len(order_status_list)):
                                raise ValueError
                            else:
                                value = order_status_list[int(index_choice)]
                                order_dict.update({keys[dict_choice] : value})
                                print(f"\tOrder status updated to {value}")
                                break
                        except ValueError:
                            print("\tInvalid choice. Please try again...")
                elif keys[dict_choice] == 'items':
                    while True:
                        try:
                            os.system('cls')
                            index_view('product',products_list)
                            o_items: List = [int(x) for x in input("\tPick products to be added / updated for this order. Use index value and separate with comma: ").split(',')]
                            if o_items != "":
                                if does_index_exist(products_list, o_items) is True:
                                    order_dict.update({keys[dict_choice] : o_items})
                                    print(f"\tOrder items updated to {o_items}")
                                    break
                                else:
                                    print("\tSelected products out of range. Please try again...")
                                    time.sleep(0.5)
                            else:
                                pass
                        except ValueError:
                            print("\tInvalid choice. Please try again...")
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
            except (ValueError, IndexError):
                print("\tInvalid choice. Please try again...")
                time.sleep(0.5)
        break
