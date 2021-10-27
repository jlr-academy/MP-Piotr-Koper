import os
from src.utils import sql_execute, sql_read, clear_screen, task_choice
from src.utils import view_all_customers, customer_id_check


#Customer Menu
def customer_menu():

    choice = ""
    while choice != 0:
        clear_screen()
        print(f"""
        Product Menu:
        ------------------------------
        [0]. Return to Main Menu
        [1]. View customers
        [2]. Create a new customer
        [3]. Update customer details
        [4]. Delete a customer""")
        choice = input("\tPlease pick a menu option: ")
        if choice == '0':
            break
        elif choice == '1':
            view_customers()
        elif choice == '2':
            add_new_customer()
        elif choice == '3':
            update_customer()
        elif choice == '4':
            delete_customer()
        else:
            print("\n \tInvalid choice. Please try again...")

#Customers View from DB
def view_customers():

    clear_screen()
    view_all_customers()
    os.system('pause')

#Adding New Customer to DB    
def add_new_customer():
    
    task_check = True
    while task_check == True:
        
        clear_screen()
        
        customer_name = input("\tCustomer name: ")
        customer_address = input("\tCustomer address: ")
        customer_phone = input("\tCustomer phone number: ")
        
        order_dict = {'customer_name': customer_name, 
                'customer_address': customer_address,
                'customer_phone': customer_phone}
        
        sql = """INSERT INTO customers(customer_name, customer_address, customer_phone) 
            VALUES(%(customer_name)s, %(customer_address)s, %(customer_phone)s)"""
        sql_execute(sql, order_dict)
        print(f"\n \tNew customer {customer_name} has beed added to the database")
        task_check = task_choice("\n \tWould you like to add another customer [y / n] ")

#Updating Customer Details in DB
def update_customer():
    
    task_check = True
    while task_check == True:
        clear_screen()
        view_all_customers()
        customer_id = customer_id_check("\n \tPlease use Id value of the customer you'd like to update? ")
        
        update_task_check = True
        while update_task_check == True:
            clear_screen()
            view_unique_customer(customer_id)
            choice = input("\n \tPlease use index value of the element you'd like to update? ").lower()
            if choice == '1':
                update_customer_name(customer_id)
            elif choice == '2':
                update_customer_address(customer_id)
            elif choice == '3':
                update_customer_phone(customer_id)
            else:
                print("\n \tInvalid input. Please try again...")
                continue
            update_task_check = task_choice("\n \tWould you like to update another element? [y / n] ")
            
        task_check = task_choice("\n \tWould you like to update another customer? [y / n] ")

def view_unique_customer(customer_id):
    
    sql = "SELECT customer_id, customer_name, customer_address, customer_phone FROM customers WHERE customer_id=%s"
    rows = sql_read(sql, customer_id)
    
    for row in rows:
        print(f"""
        [1]. - Customer Name: {str(row[1])}
        [2]. - Customer Address: {row[2]}
        [3]. - Customer Phone: {row[3]}""")

def update_customer_name(customer_id):
    
    name = input("\n \tWhat is customer's new name? " )
    if name == "":
        return
    else:
        data = (name, customer_id)
        sql = "UPDATE customers SET customer_name=%s WHERE customer_id=%s"
        sql_execute(sql, data)

def update_customer_address(customer_id):
    
    address = input("\n \tWhat is customer's new address? " )
    if address == "":
        return
    else:
        data = (address, customer_id)
        sql = "UPDATE customers SET customer_address=%s WHERE customer_id=%s"
        sql_execute(sql, data)

def update_customer_phone(customer_id):
    
    phone = input("\n \tWhat is customer's new phone number? " )
    if phone == "":
        return
    else:
        data = (phone, customer_id)
        sql = "UPDATE customers SET customer_phone=%s WHERE customer_id=%s"
        sql_execute(sql, data)

#Deleteting Customer from DB
def delete_customer():
    task_check = True
    while task_check == True:

        customer_id = customer_id_check("\n \tPlease use Id value of the customer you'd like to delete? ")
        
        sql = "SELECT order_id FROM orders WHERE customer_id=%s"
        data_check = sql_read(sql, customer_id)
        
        if not data_check:
            sql_2 = "DELETE FROM customers WHERE customer_id=%s"
            sql_execute(sql_2, customer_id)

            print("\n \tCustomer Id {customer_id} has been deleted from the database." )

        else:
            customer_db_purge(customer_id)
        
        task_check = task_choice("\n \tWould you like to delete another customer? [y / n] ")


def customer_db_purge(customer_id):
    
    print(f"\n \tSelected customer Id: {customer_id} is part of the following order(s):")
                        
    sql = """SELECT orders.order_id, orders.customer_id, order_status.order_status
        FROM orders
        LEFT JOIN order_status
        ON orders.status_id = order_status.status_id
        WHERE orders.customer_id=%s
        """
    rows = sql_read(sql, customer_id)
    print(f"\n \t{'Order Id:' :<13} | {'Customer Id:' :<13} | {'Order Status:' :<15} ")
    for row in rows:
        print(f"\t{row[0] :<13} | {row[1] :<13} | {row[2] :<15} ")

    while True:
        choice = input("\n \tWould you like to proceed and delete all orders associated to this customer and customer itself from entire database? [y / n] ").lower()
        if choice == 'y':
            
            sql = "SELECT order_id FROM orders WHERE customer_id=%s"
            rows = sql_read(sql, customer_id)
            for row in rows:
                order_id = row[0]
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
                
                sql = "DELETE FROM orders_products WHERE order_id=%s"
                sql_execute(sql, row[0])
            
            print("\n \tCustomer Id {customer_id} and all associated orders have been deleted from database." )
            
            sql = "DELETE FROM orders WHERE customer_id=%s"
            sql_execute(sql, customer_id)
            
            sql = "DELETE FROM customers WHERE customer_id=%s"
            sql_execute(sql, customer_id)
            
            print("\n \tCustomer and all associated orders have been deleted from database." )
            
            break
            
        elif choice == 'n':
            break
        else:
            print("\n \tInvalid choice. Please try again...")