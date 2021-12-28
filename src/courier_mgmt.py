import os
from src.utils import sql_read, sql_execute, clear_screen
from src.utils import upper_case_conversion, task_choice
from src.utils import view_all_couriers, courier_id_check

#Curier Menu
def courier_menu():

    choice = ""
    while choice != 0:
        clear_screen()
        print(f"""
        Courier Menu:
        ------------------------------
        [0]. Return to Main Menu
        [1]. View couriers
        [2]. Create a new courier
        [3]. Update courier details
        [4]. Delete a courier""")
        choice = input("\tPlease pick a menu option: ")
        if choice == '0':
            break
        elif choice == '1':
            view_couriers()
        elif choice == '2':
            add_new_courier()
        elif choice == '3':
            update_courier()
        elif choice == '4':
            delete_courier()
        else:
            print("\n \tInvalid choice. Please try again...")

#Couerirs View from DB
def view_couriers():

    clear_screen()
    view_all_couriers()
    os.system('pause')


#Adding New Courier to DB
def add_new_courier():
    
    task_check = True
    while task_check == True:
        
        clear_screen()
        name = upper_case_conversion(input("\n \tWhat is the new courier name? "))
        phone = input(f"\n \tWhat is courier's phone number? ")
        
        couriers_dict = {'name': name, 'phone': phone}
        sql = """INSERT INTO couriers (name, phone) 
                VALUES(%(name)s, %(phone)s)"""
        sql_execute(sql, couriers_dict)
        print(f"\n \tCourier {name} has beed added to the database")
        task_check = task_choice("\n \tWould you like to add another courier [y / n] ")


#Updating Courier
def update_courier():
    
    task_check = True
    while task_check == True:
        id_choice = courier_id_check("\n \tPlease use Id value for the courier you'd like to update? ")
        
        update_task_check = True
        while update_task_check == True:
            clear_screen()
            view_unique_courier(id_choice)
            el_choice = input("\n \tPlease use index value of the element you'd like to update? ")
            if el_choice == '1'or el_choice == 'name':
                update_courier_name(id_choice)
            elif el_choice == '2'or el_choice == 'phone':
                update_courier_phone(id_choice)
            else:
                print("\n \tInvalid input. Please try again...")
                continue
            update_task_check = task_choice("\n \tWould you like to update another element? [y / n] ")
            
        task_check = task_choice("\n \tWould you like to update another courier? [y / n] ")

def view_unique_courier(id_choice):
    
    sql = "SELECT courier_id, name, phone FROM couriers WHERE courier_id=%s"
    rows = sql_read(sql, id_choice)
    
    for row in rows:
        print(f"""
        [1]. - Name: {str(row[1])}
        [2]. - Phone: {row[2]}""")

def update_courier_name(id_choice):
    
    name = input("\n \t What is courier's new name? ")
    data = (name, id_choice)
    sql = "UPDATE couriers SET name=%s WHERE courier_id=%s"
    
    if name == "":
        pass
    else:
        sql_execute(sql, data)

def update_courier_phone(id_choice):
    
    phone = input("\n \tWhat is courier's new phone number? ")
    data = (phone, id_choice)
    sql = "UPDATE couriers SET phone=%s WHERE courier_id=%s"
    
    if phone == "":
        pass
    else:
        sql_execute(sql, data)


#Deleteting Courier from DB
def delete_courier():
    task_check = True
    while task_check == True:

        courier_id = courier_id_check("\n \tPlease use Id value of the courier you'd like to delete? ")
        
        sql = "SELECT order_id FROM orders WHERE courier_id=%s"
        data_check = sql_read(sql, courier_id)
        
        if not data_check:
            sql_2 = "DELETE FROM couriers WHERE courier_id=%s"
            sql_execute(sql_2, courier_id)

            print(f"\n \tCourier Id {courier_id} has been deleted from the database")

        else:
            courier_db_purge(courier_id)
        
        task_check = task_choice("\n \tWould you like to delete another courier? [y / n] ")


def courier_db_purge(courier_id):
    
    print(f"\n \tSelected courier Id: {courier_id} is part of the following order(s):")
                        
    sql = """SELECT orders.order_id, orders.courier_id, order_status.order_status
        FROM orders
        LEFT JOIN order_status
        ON orders.status_id = order_status.status_id
        WHERE orders.courier_id=%s
        """
    rows = sql_read(sql, courier_id)
    print(f"\n \t{'Order Id:' :<13} | {'Courier Id:' :<13} | {'Order Status:' :<15} ")
    for row in rows:
        print(f"\t{row[0] :<13} | {row[1] :<13} | {row[2] :<15} ")
    
    while True:
        choice = input("\n \tWould you like to proceed and delete all orders associated with this courier and courier itself from entire database? [y / n] ").lower()
        if choice == 'y':
            
            sql = "SELECT order_id FROM orders WHERE courier_id=%s"
            rows = sql_read(sql, courier_id)
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
                sql_execute(sql, order_id)
            
            print(f"\n \tCourier Id {courier_id} and all associated orders have been deleted from the database." )
            
            sql = "DELETE FROM orders WHERE courier_id=%s"
            sql_execute(sql, courier_id)
            
            sql = "DELETE FROM couriers WHERE courier_id=%s"
            sql_execute(sql, courier_id)
            
            break
        elif choice == 'n':
            break
        else:
            print("\n \tInvalid choice. Please try again...")
