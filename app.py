import time
from src.utils import clear_screen
from src.product_mgmt import product_menu
from src.courier_mgmt import courier_menu
from src.order_mgmt import orders_menu

# products = [Product(1, 'Tea', 1.0, 20),Product(1, 'Plum', 5.0, 100)]

# Main Function
def main():
    
    # products_list = load_data('products')
    # couriers_list = load_data('couriers')
    # orders_list = load_data('orders')
    # order_status_list = ['preparing', 'finalizing', 'completed']

    main_menu()

#Main Menu Function - COMPLETE
def main_menu():

    choice = ""
    while choice != 0:
        clear_screen()
        print("""
        Main Menu:
        -------------------
        [0]. Exit App
        [1]. Product Menu
        [2]. Courier Menu
        [3]. Order Menu""")
        choice = input("\tPlease pick a menu option: ")
        if choice == '0':
            exit()  
        elif choice == '1':
            product_menu()
        elif choice == '2':
            courier_menu()
        elif choice == '3':
            orders_menu()
        else:
            print("\n \tInvalid choice. Please try again...")

#App Exit and Save Files Function - COMPLETE
def save_and_exit():
    
    # save_data('orders', orders_list, cursor)
    # save_data('products', orders_list, cursor)
    # save_data('couriers', orders_list, cursor)
    
    print("""
    \tAll files updated and saved.
    \tApp is closing....""")
    
    time.sleep(1)
    exit()

if __name__ == "__main__":
    main()
