import os
from utils import products_view_all, clear_screen, task_choice
from utils import float_input_check, int_input_check
from utils import product_name_duplicate_check, product_id_check

#Products & Couriers Menu Function - COMPLETE
def product_menu(connection, cursor):

    choice = ""
    while choice != 0:
        clear_screen()
        print(f"""
        Product Menu:
        ------------------------------
        [0]. Return to Main Menu
        [1]. View products list
        [2]. Create a new product
        [3]. Update product details
        [4]. Delete product""")
        choice = input("\tPlease pick a menu option: ")
        if choice == '0':
            break
        elif choice == '1':
            products_view(cursor)
        elif choice == '2':
            add_new_product(connection, cursor)
        elif choice == '3':
            product_update(connection, cursor)
        elif choice == '4':
            product_delete(connection, cursor)
        else:
            print("Invalid choice. Please try again...")

#Products View from DB
def products_view(cursor):

    clear_screen()
    products_view_all(cursor)
    os.system('pause')

#Adding New Product to DB
def add_new_product(connection, cursor):
    task_check = True
    while task_check == True:
        clear_screen()
        name = product_name_duplicate_check(cursor, "\n \tWhat is the new product name? ")
        price = float_input_check("\n \tWhat is the product price? ")
        # qty = int_input_check(input("\tPlease confirm product quantity: "))
        cursor.execute("INSERT INTO products(name, price) VALUES(%s, %s)",(name, price))
        connection.commit()
        print(f"\n \t{name} with price of {price} has beed added to the database")
        task_check = task_choice("\n \tWould you like to add another product [y / n] ")

#Updating Product Details in DB
def product_update(connection, cursor):
    task_check = True
    while task_check == True:
        clear_screen()
        products_view_all(cursor)
        id_choice = product_id_check(cursor, "\n \tPlease use Id value for the product you'd like to update? ")
        cursor.execute("SELECT product_id, name, price FROM products WHERE product_id=%s",(id_choice))
        rows = cursor.fetchall()
        update_task_check = True
        while update_task_check == True:
            clear_screen()
            for row in rows:
                print(f"\t[1]. - Name: {str(row[1])}")
                print(f"\t[2]. - Price: {row[2]}")
            el_choice = input("\n \tPlease use index value of the element you'd like to update? ")
            if el_choice == '1':
                name = product_name_duplicate_check(cursor, "\n \tWhat is product's new name? " )
                if name == "":
                    pass
                else:
                    cursor.execute("UPDATE products SET name=%s WHERE product_id=%s",(name, id_choice))
                    connection.commit()
            elif el_choice == '2':
                price = float_input_check(input("\n \tWhat is the product's new price? "))
                if price == "":
                    pass
                else:
                    cursor.execute("UPDATE products SET price=%s WHERE product_id=%s",(price, id_choice))
                    connection.commit()
            else:
                print("\n \tInvalid input. Please try again...")
                continue
            update_task_check = task_choice("\n \tWould you like to update another element? [y / n] ")
        task_check = task_choice("\n \tWould you like to update another product? [y / n] ")

#Deleteting Product from DB
def product_delete(connection, cursor):
    task_check = True
    while task_check == True:
        clear_screen()
        products_view_all(cursor)
        id_choice = product_id_check(cursor, "\n \tPlease use Id value for product you'd like to delete? ")
        cursor.execute("DELETE FROM products WHERE product_id=%s", (id_choice))
        connection.commit()
        task_check = task_choice("\n \tWould you like to delete another product? [y / n] ")