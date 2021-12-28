import time
from src.utils import clear_screen
from src.product_mgmt import product_menu
from src.courier_mgmt import courier_menu
from src.order_mgmt import orders_menu
from src.customer_mgmt  import customer_menu
from src.file_handler import save_data

# Main Function
def main():

    # products_list = load_data('products')
    # couriers_list = load_data('couriers')
    # orders_list = load_data('orders')


    main_menu()

#Main Menu
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
        [3]. Order Menu
        [4]. Customer Menu""")
        choice = input("\tPlease pick a menu option: ")
        if choice == '0':
            exit()  
        elif choice == '1':
            product_menu()
        elif choice == '2':
            courier_menu()
        elif choice == '3':
            orders_menu()
        elif choice == '4':
            customer_menu()
        else:
            print("\n \tInvalid choice. Please try again...")

#App Exit and Save Files data to CSV
def save_and_exit():
    
    save_data('orders')
    save_data('products')
    save_data('couriers')
    
    print("""
    \tAll files updated and saved.
    \tApp is closing....""")
    
    time.sleep(1)
    exit()

if __name__ == "__main__":
    main()
