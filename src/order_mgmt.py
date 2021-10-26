import os
import time
from src.utils import sql_read, sql_execute, clear_screen
from src.utils import order_id_check, order_status_check

from src.utils import view_all_orders, task_choice, courier_id_check
from src.utils import task_choice, customer_review, order_items_review

#Order Menu Function - COMPLETE
def orders_menu():
    choice = []
    while choice != 0:
        clear_screen()
        print("""
        Orders Menu:
        ------------------------------
        [0]. Return to Main Menu
        [1]. View orders
        [2]. Create a new order
        [3]. Update order status
        [4]. Update existing order
        [5]. Delete order""")
        choice = input("\tPlease pick a menu option: ")
        if choice == '0':
            break
        elif choice == '1':
            orders_view()
        elif choice == '2':
            add_new_order()
        elif choice == '3':
            update_order_status()
        elif choice == '4':
            print("Under development")
        elif choice == '5':
            print("Under development")
        else:
            print("Invalid choice. Please try again...")

#Orders View from DB
def orders_view():
    
    clear_screen()
    view_all_orders()
    os.system('pause')

#Adding New Order to DB
def add_new_order():

    task_check = True
    while task_check == True:
        clear_screen()
        print("\tPlease provide new order details such us: Customer Details, Couirer, Products & Quantities")
        os.system('pause')
        customer_id = customer_review()
        courier_id = courier_id_check("\n \tPlease use Id value of the couirer you'd like to assign to this order? ")
        status_id = "1"

        order_dict = {'customer_id': customer_id, 
                    'courier_id': courier_id,
                    'status_id': status_id}

        sql = """INSERT INTO orders(customer_id, courier_id, status_id) 
                VALUES(%(customer_id)s, %(courier_id)s, %(status_id)s)"""
        sql_execute(sql, order_dict)

        sql = """SELECT order_id FROM orders
                WHERE customer_id=%(customer_id)s AND courier_id=%(courier_id)s AND status_id=%(status_id)s"""
        rows = sql_read(sql, order_dict)
        for row in rows:
            order_id = row[0]
        order_items_review(order_id)

        print("\n \tOrder has beed added to the database and status assigned to preparing")
        task_check = task_choice("\n \tWould you like to add another order [y / n] ")

def update_order_status():
    
    task_check = True
    while task_check == True:
        id_choice = order_id_check("\n \tPlease use Id value of the order you'd like to update: ")
        order_status = order_status_check("\tPlease use Id value for new order status: ")
        data = (order_status, id_choice)
        sql = "UPDATE orders SET status_id=%s WHERE order_id=%s"
        sql_execute(sql, data)
        print("\n \t Order status has been updated")
        task_check = task_choice("\n \tWould you like to update another order status [y / n] ")

def update_order():
    
    task_check = True
    while task_check == True:
        clear_screen()
        view_all_orders()
        id_choice = order_id_check("\n \tPlease use Id value of the order you'd like to update? ")
        
    pass


def view_unique_order(id_choice):
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






def delete_order():
    
    task_check = True
    while task_check == True:
        clear_screen()
        view_all_orders()
        id_choice = order_id_check("\n \tPlease use Id value of the order you'd like to delete? ")
        sql = "DELETE FROM orders WHERE order_id=%s"
        sql_execute(sql, id_choice)
        task_check = task_choice("\n \tWould you like to delete another order? [y / n] ")
    


















#Print all orders by defoult, courier or list
#To improve User interaction
# def orders_view():
#     while True:
#         try:
#             os.system('cls')
#             print("""
#         Please select the way you'd like to preview orders [ sorted by ]:
#         [1]. Default
#         [2]. Status 
#         [3]. Courier""")
#             choice = input("\t")
#             if choice =='1':
#                 index_view('orders', orders_list)
#                 os.system('pause')
#                 break
#             elif choice == '2':
#                 sorted(orders_list, key=lambda x: x.get('status'))
#                 index_view('orders', orders_list)
#                 os.system('pause')
#                 break
#             elif choice == '3':
#                 sorted(orders_list, key=lambda x: x.get('courier'))
#                 index_view('orders', orders_list)
#                 os.system('pause')
#                 break
#             else:
#                 raise ValueError
#         except ValueError:
#             print("")
#             print("\tInvalid choice. Please try again...")
#             time.sleep(0.5)
        
# #Adding new Order Function - COMPLETE
# def add_new_order():
#     check = True
#     while check == True:
#         os.system('CLS')
#         print("\tPlease provide new order details:")
#         o_customer_name = input("\tCustomer name: ")
#         o_customer_address = input("\tCustomer address: ")
#         o_customer_phone = input("\tCustomer phone number: ")
#         o_courier = courier_id_choice("\n \tPlease use Id for the courier you'd like to assign to this order ")
#         o_status = "preparing"
#         o_items =  add_items_to_order(products_list, 'added')
#         order_dic = {
#             "customer_name": o_customer_name,
#             "customer_address": o_customer_address,
#             "customer_phone": o_customer_phone,
#             "courier": o_courier,
#             "status": o_status,
#             "items": o_items
#         }
#         orders_list.append(order_dic)
#         print("\tOrder logged and status set to 'PREPARIG'...")
#         time.sleep(2)
#         check = end_of_task_choice('order', 'add')

# #Checking if products exist in product_list and if yes add them to the order        
# def add_items_to_order():
#     while True:
#         try:
#             os.system('cls')
#             index_view('product', products_list)
#             o_items = [int(x) for x in input(f"\tPlease use index value separated with comma for product(s) to be {task} to this order. ").split(',')]
#             if does_index_exist(products_list, o_items) is True:
#                 return o_items
#             else:
#                 print("")
#                 print("\tSelected products out of range. Please try again...")
#                 time.sleep(0.5)  
#         except ValueError:
#             print("")
#             print("\tInvalid choice. Please try again...")
#             time.sleep(0.5)

# #Updating Order Status Function - COMPLETE
# def order_status_updt():
    
#     check = True
#     while check == True:
#         o_idx_choice = user_idx_choice('order', orders_list, 'updated')
#         os_idx_choice = user_idx_choice('order status', order_status_list, 'updated')
#         order_dic = orders_list[o_idx_choice]
#         order_dic["status"] = order_status_list[os_idx_choice]
#         print(f"\tOrder status has been updated to {order_status_list[os_idx_choice]}")
#         time.sleep(0.5)
#         check = end_of_task_choice('order status', 'update')

# #Updating Order Details Function - COMPLETE
# def order_updt():
#     while True:
#         o_idx_choice = user_idx_choice('order', orders_list, 'updated')
#         while True:
#             try:
#                 os.system('cls')
#                 order_dict: Dict = orders_list[o_idx_choice]
#                 print(f"\tCustomer order details:")
#                 for index, (key, value) in enumerate(order_dict.items()):
#                     print(f"\t[{index}] - {key} - {value}")
#                 keys = list(order_dict)
#                 dict_choice = int(input("\tPlease use index value for order element to be update: "))
#                 if keys[dict_choice] == 'courier':
#                     while True:
#                         try:
#                             os.system('cls')
#                             index_view('courier', couriers_list)
#                             value = input("\tPlease use index value for new courier to be assigned: ")
#                             if value == "":
#                                 break
#                             elif int(value) not in range(len(couriers_list)):
#                                 raise ValueError
#                             else:    
#                                 order_dict.update({keys[dict_choice] : int(value)})
#                                 print(f"\tCourier updated to {value}: {couriers_list[int(value)]}")
#                                 break
#                         except ValueError:
#                             print("\tInvalid choice. Please try again...")
#                 elif keys[dict_choice] == 'status':
#                     while True:
#                         try:
#                             os.system('cls')
#                             index_view('status', order_status_list)
#                             index_choice = input(f"\tPlease use index value for new order status to be assigned: ")
#                             if index_choice == "":
#                                 break
#                             elif int(index_choice) not in range(len(order_status_list)):
#                                 raise ValueError
#                             else:
#                                 value = order_status_list[int(index_choice)]
#                                 order_dict.update({keys[dict_choice] : value})
#                                 print(f"\tOrder status updated to {value}")
#                                 break
#                         except ValueError:
#                             print("\tInvalid choice. Please try again...")
#                 elif keys[dict_choice] == 'items':
#                     while True:
#                         try:
#                             os.system('cls')
#                             index_view('product',products_list)
#                             o_items: List = [int(x) for x in input("\tPick products to be added / updated for this order. Use index value and separate with comma: ").split(',')]
#                             if o_items != "":
#                                 if does_index_exist(products_list, o_items) is True:
#                                     order_dict.update({keys[dict_choice] : o_items})
#                                     print(f"\tOrder items updated to {o_items}")
#                                     break
#                                 else:
#                                     print("\tSelected products out of range. Please try again...")
#                                     time.sleep(0.5)
#                             else:
#                                 pass
#                         except ValueError:
#                             print("\tInvalid choice. Please try again...")
#                 else:
#                     value = input(f"\tWhat is the new {keys[dict_choice]}: ")
#                     if value != "":
#                         order_dict.update({keys[dict_choice] : value})
#                     else:
#                         pass
#                 decision = input("\tWould you like to change another element? (y / n) ")
#                 if decision == 'y':
#                     pass
#                 else:
#                     break
#             except (ValueError, IndexError):
#                 print("\tInvalid choice. Please try again...")
#                 time.sleep(0.5)
#         break
