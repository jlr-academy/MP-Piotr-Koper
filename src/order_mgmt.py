import os
import time

from src.utils import sql_read, sql_execute, clear_screen
from src.utils import order_id_check, order_status_check, int_input_check
from src.utils import view_all_orders, task_choice, courier_id_check, product_stock_check
from src.utils import task_choice, customer_review, view_all_products, product_id_check

#Order Menu
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
        [5]. Delete an order""")
        choice = input("\tPlease pick a menu option: ")
        if choice == '0':
            break
        elif choice == '1':
            view_orders()
        elif choice == '2':
            add_new_order()
        elif choice == '3':
            update_order_status()
        elif choice == '4':
            update_order()
        elif choice == '5':
            delete_order()
        else:
            print("Invalid choice. Please try again...")

#Orders View from DB
def view_orders():
    
    clear_screen()
    view_all_orders()
    os.system('pause')


#Adding New Order to DB
def add_new_order():

    task_check = True
    while task_check == True:
        clear_screen()
        print("\n \tPlease provide new order details such us: Customer Details, Couirer, Products & Quantities")
        os.system('pause')
        customer_id = customer_review()
        courier_id = courier_id_check("\n \tPlease use Id value of the courier you'd like to assign to this order? ")
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
        add_order_items(order_id)

        print("\n \tOrder has beed added to the database and status assigned to preparing")
        task_check = task_choice("\n \tWould you like to add another order [y / n] ")

def add_order_items(order_id):
    
    task_check = True
    while task_check == True:

        product_id = product_id_check("\n \tPlease use Id value of the product you'd like to have in the order? ")
        quantity = product_stock_check(product_id, "\n \tHow many would you like to order? ")
        data = (order_id, product_id, quantity)
        sql = """INSERT INTO orders_products(order_id, product_id, quantity) 
                VALUES(%s, %s, %s)"""
        sql_execute(sql, data)

        task_check = task_choice("\n \tWould you like to add another product to this order? [y / n] ")


#Updating Order Status
def update_order_status(id_choice=None):
    
    if id_choice == None:
        task_check = True
        while task_check == True:
            id_choice = order_id_check("\n \tPlease use Id value of the order you'd like to update: ")
            order_status = order_status_check("\tPlease use Id value for new order status: ")
            data = (order_status, id_choice)
            sql = "UPDATE orders SET status_id=%s WHERE order_id=%s"
            sql_execute(sql, data)
            print("\n \tOrder status has been updated")
            task_check = task_choice("\n \tWould you like to update another order status [y / n] ")
    else:
        order_status = order_status_check("\tPlease use Id value for new order status: ")
        data = (order_status, id_choice)
        sql = "UPDATE orders SET status_id=%s WHERE order_id=%s"
        sql_execute(sql, data)


#Updating Order Details
def update_order():
    
    task_check = True
    while task_check == True:
        clear_screen()
        view_all_orders()
        order_id = order_id_check("\n \tPlease use Id value of the order you'd like to update? ")
        
        update_task_check = True
        while update_task_check == True:
            clear_screen()
            view_unique_order(order_id)
            el_choice = input("\n \tPlease use index value of the order element you'd like to update? ").lower()
            if el_choice == '1':
                update_order_customer(order_id)
            elif el_choice == '2':
                update_order_courier(order_id)
            elif el_choice == '3':
                update_order_status(order_id)
            elif el_choice == '4':
                update_order_items(order_id)
            else:
                print("\n \tInvalid input. Please try again...")
                continue
            update_task_check = task_choice("\n \tWould you like to update another order element? [y / n] ")
            
        task_check = task_choice("\n \tWould you like to update another order? [y / n] ")

def view_unique_order(order_id):
    sql = """SELECT orders.order_id, customers.customer_name, customers.customer_address, customers.customer_phone, 
                    couriers.courier_id, order_status.order_status, orders_products.product_id, orders_products.quantity
                FROM orders
                LEFT JOIN customers
                ON orders.customer_id = customers.customer_id
                LEFT JOIN couriers
                ON orders.courier_id = couriers.courier_id
                LEFT JOIN order_status
                ON orders.status_id = order_status.status_id
                JOIN orders_products
                ON orders.order_id = orders_products.order_id
                WHERE orders.order_id=%s
                """
    rows = sql_read(sql, order_id)
    print(f"\n \t{'Id:' :<7} | {'Customer Name:' :<17} | {'Customer Address:' :<50} | {'Customer Phone:' :<15} | {'Courier Id:' :<13} | {'Order Status:' :<15} | {'Product Id:' :<13} | {'Quantity:' :<10} ")
    for row in rows:
        print(f"\t{row[0] :<7} | {str(row[1]) :<17} | {row[2] :<50} | {row[3] :<15} | {row[4] :<13} | {row[5] :<15} | {row[6] :<13} | {row[7] :<10} ")

    print(f"""
        [1]. - Customer
        [2]. - Courier
        [3]. - Order Status
        [4]. - Product(s) and Quantity""")

def update_order_customer(order_id):
    
    customer_id = customer_review()
    data = (customer_id, order_id)
    sql = "UPDATE orders SET customer_id=%s WHERE order_id=%s"
    sql_execute(sql, data)

def update_order_courier(order_id):
    
    courier_id = courier_id_check("\n \tPlease use Id value of the courier you'd like to assign to this order? ")
    data = (courier_id, order_id)
    sql = "UPDATE orders SET courier_id=%s WHERE order_id=%s"
    sql_execute(sql, data)

def update_order_items(order_id):
    
    task_check = True
    while task_check == True:
        clear_screen()
        sql = """SELECT orders_products.order_id, orders_products.product_id, products.name, orders_products.quantity
                    FROM orders_products
                    LEFT JOIN products
                    ON orders_products.product_id = products.product_id
                    WHERE order_id=%s
                    """
        rows = sql_read(sql, order_id)
        print(f"\n \t{'Order Id:' :<10} | {'Product Id:' :<12} | {'Product Name:' :<15} | {'Quantity:' :<10} ")
        for row in rows:
            print(f"\t{row[0] :<10} | {row[1] :<12} | {row[2] :<15} | {row[3] :<10}")
        
        print("""
        [1]. Add a new product to the order
        [2]. Update existing product quantity
        [3]. Delete specific product from an order""")
        choice = input("\n \tPlease use index value of the activity you'd like to complete? ").lower()
        if choice == '1':
            add_order_items(order_id)
        elif choice == '2':
            update_order_items_qty(order_id)
        elif choice == '3':
            delete_order_items(order_id)
        else:
            print("\n \tInvalid input. Please try again...")
        task_check = task_choice("\n \tWould you like to complete another order-product activity? [y / n] ")

def update_order_items_qty(order_id):
    
    task_check = True
    while task_check == True:
        product_id = int_input_check("\n \tWhich Product Id you'd like to update qty for? ") #Error handler req
        
        sql = "SELECT stock FROM products WHERE product_id=%s"
        rows = sql_read(sql, product_id)
        for row in rows:
            stock = row[0]
        
        while True:
            print(f"\n \tThere is/are {stock} available in stock")
            
            new_qty = int_input_check("\n \tWhat is the new quantity you'd like to assign to the order? ")
            
            sql = "SELECT quantity FROM orders_products WHERE product_id=%s AND order_id=%s"
            data = (product_id, order_id)
            rows = sql_read(sql, data)
            for row in rows:
                order_qty = row[0]
            
            if (new_qty > order_qty) and (new_qty - order_qty) > stock:
                print(f"\n \tThere isn't enough in stock. Please use smaller amount...")
                time.sleep(1)
            else:
                sql = "UPDATE orders_products SET quantity=%s WHERE product_id=%s AND order_id=%s"
                data = (new_qty, product_id, order_id)
                sql_execute(sql, data)
                
                sql = "UPDATE products SET stock=%s WHERE product_id=%s"
                new_stock = stock - (new_qty-order_qty)
                data = (new_stock, product_id)
                sql_execute(sql, data)
                break
        task_check = task_choice("\n \tWould you like to add, delete or update another product qty? [y / n] ")

def delete_order_items(order_id):
    
    task_check = True
    while task_check == True:
        product_id = int_input_check("\n \tPlease use Product Id value of the product you'd like to remove? ") #Error handler req
        
        sql = "SELECT quantity FROM orders_products WHERE order_id=%s AND product_id=%s"
        data = (order_id, product_id)
        rows = sql_read(sql, data)
        for row in rows:
            qty = row[0] 
        
        sql = "SELECT stock FROM products WHERE product_id=%s"
        rows = sql_read(sql, product_id)
        for row in rows:
            stock = row[0] 
        
        new_stock = stock + qty
        
        sql = """UPDATE products SET stock=%s WHERE product_id=%s"""
        data(new_stock, product_id)
        sql_execute(sql, data)
        
        sql = "DELETE FROM orders_products WHERE product_id=%s"
        sql_execute(sql, product_id)
        
        task_check = task_choice("\n \tWould you like to delete another product? [y / n] ")


#Deleting an Order
def delete_order():
    
    task_check = True
    while task_check == True:

        order_id = order_id_check("\n \tPlease use Id value of the order you'd like to delete? ")
        
        sql = "SELECT product_id FROM orders_products WHERE order_id=%s"
        rows = sql_read(sql, order_id)
        for row in rows:
            product_id = row[0]
            sql = "SELECT quantity FROM orders_products WHERE order_id=%s AND product_id=%s"
            data = (order_id, product_id)
            qrows = sql_read(sql, data)
            for qrow in qrows:
                qty = qrow[0] 
            
            sql = "SELECT stock FROM products WHERE product_id=%s"
            srows = sql_read(sql, product_id)
            for srow in srows:
                stock = srow[0] 
            
            new_stock = (stock + qty)
            
            sql = """UPDATE products SET stock=%s WHERE product_id=%s"""
            data = (new_stock, product_id)
            sql_execute(sql, data) 

        print("\n \tOrder Id {order_id} has been deleted from the database")

        sql = "DELETE FROM orders_products WHERE order_id=%s"
        sql_execute(sql, order_id)

        sql = "DELETE FROM orders WHERE order_id=%s"
        sql_execute(sql, order_id)

        task_check = task_choice("\n \tWould you like to delete another order? [y / n] ")
