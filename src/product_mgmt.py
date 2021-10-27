import os
from src.utils import sql_read, sql_execute, clear_screen, task_choice
from src.utils import float_input_check, int_input_check, view_all_products
from src.utils import product_name_duplicate_check, product_id_check, view_unique_product

#Product Menu
def product_menu():

    choice = ""
    while choice != 0:
        clear_screen()
        print(f"""
        Product Menu:
        ------------------------------
        [0]. Return to Main Menu
        [1]. View products
        [2]. Create a new product
        [3]. Update product details
        [4]. Delete a product""")
        choice = input("\tPlease pick a menu option: ")
        if choice == '0':
            break
        elif choice == '1':
            view_products()
        elif choice == '2':
            add_new_product()
        elif choice == '3':
            update_product()
        elif choice == '4':
            delete_product()
        else:
            print("\n \tInvalid choice. Please try again...")

#Products View from DB
def view_products():

    clear_screen()
    view_all_products()
    os.system('pause')


#Adding New Product to DB
def add_new_product():
    
    task_check = True
    while task_check == True:
        
        clear_screen()
        name = product_name_duplicate_check( "\n \tWhat is the new product name? ")
        price = float_input_check("\n \tWhat is the product price? ")
        stock = int_input_check("\n \tPlease confirm product quantity: ")
        
        product_dict = {'name': name, 'price': price, 'stock': stock}
        
        sql = """INSERT INTO products(name, price, stock) 
                VALUES(%(name)s, %(price)s, %(stock)s)"""
        sql_execute(sql, product_dict)
        print(f"\n \t{name} with quantity of [ {stock} ] and price of £{price} has beed added to the database")
        task_check = task_choice("\n \tWould you like to add another product [y / n] ")


#Updating Product Details in DB
def update_product():
    
    task_check = True
    while task_check == True:
        
        product_id = product_id_check("\n \tPlease use Id value of the product you'd like to update? ")
        
        update_task_check = True
        while update_task_check == True:
            clear_screen()
            view_unique_product(product_id)
            choice = input("\n \tPlease use index value of the element you'd like to update? ").lower()
            if choice == '1' or choice == 'name':
                update_product_name(product_id)
            elif choice == '2' or choice == 'price':
                update_product_price(product_id)
            elif choice == '3' or choice == 'stock':
                update_product_qty(product_id)
            else:
                print("\n \tInvalid input. Please try again...")
                continue
            update_task_check = task_choice("\n \tWould you like to update another element? [y / n] ")
            
        task_check = task_choice("\n \tWould you like to update another product? [y / n] ")

def update_product_name(id_choice):
    
    name = product_name_duplicate_check("\n \tWhat is product's new name? " )
    if name == "":
        return
    else:
        data = (name, id_choice)
        sql = "UPDATE products SET name=%s WHERE product_id=%s"
        sql_execute(sql, data)

def update_product_price(id_choice):
    
    price = float_input_check("\n \tWhat is the product's new price? ")
    if price == "":
        return
    else:
        sql = "UPDATE products SET price=%s WHERE product_id=%s"
        data = (price, id_choice)
        sql_execute(sql, data)

def update_product_qty(id_choice):
    
    stock = int_input_check("\n \tWhat is the product's new quantity? ")
    if stock == "":
        return
    else:
        sql = "UPDATE products SET stock=%s WHERE product_id=%s"
        data = (stock, id_choice)
        sql_execute(sql, data)


#Deleteting Product from DB
def delete_product():
    
    task_check = True
    while task_check == True:

        product_id = product_id_check("\n \tPlease use Id value of the product you'd like to delete? ")
        
        sql = "SELECT product_id FROM orders_products WHERE product_id=%s"
        data_check = sql_read(sql, product_id)
        if not data_check:
            sql = "DELETE FROM products WHERE product_id=%s"
            sql_execute(sql, product_id)
        else:
            print(f"\n \tSelected product Id: {product_id} is part of the following order(s):")
                        
            sql = """SELECT orders.order_id, orders_products.product_id, orders_products.quantity, order_status.order_status
                FROM orders
                LEFT JOIN order_status
                ON orders.status_id = order_status.status_id
                JOIN orders_products
                ON orders.order_id = orders_products.order_id
                WHERE orders_products.product_id=%s
                """
            rows = sql_read(sql, product_id)
            print(f"\n \t{'Order Id:' :<13} | {'Product Id:' :<13} | {'Quantity:' :<10} | {'Order Status:' :<15} ")
            for row in rows:
                print(f"\t{row[0] :<13} | {row[1] :<13} | {row[2] :<10} | {row[3] :<15} ")
            
            while True:
                choice = input("\n \tWould you like to proceed and delete this product from all existing orders and entire database? [y / n] ").lower()
                if choice == 'y':
                    
                    sql = "DELETE FROM orders_products WHERE product_id=%s"
                    sql_execute(sql, product_id)
                    
                    sql = "DELETE FROM products WHERE product_id=%s"
                    sql_execute(sql, product_id)
                    
                    break
                    
                elif choice == 'n':
                    break
                else:
                    print("\n \tInvalid choice. Please try again...")
        task_check = task_choice("\n \tWould you like to delete another product? [y / n] ")
    


