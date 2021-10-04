
import os
import time
from file_handler import load_data, save_data

products_list = []
couriers_list = []
load_data(products_list, couriers_list)

#Main Menu Function
def main_menu():
    while True:
        try:
            os.system('CLS')
            mm_options = int(input("""
                            0. Exit App
                            1. Product Menu
                            2. Courier Menu
                            
                            Please Pick Required Menu Option: """))
            if mm_options in [0,1,2]:
                if mm_options == 0:
                    save_and_exit()                        
                elif mm_options == 1:
                    sub_menu("Product", products_list)
                elif mm_options == 2:
                    sub_menu("Courier", couriers_list)
            else:
                raise ValueError 
        except (TypeError, ValueError):
            print("\n Wrong option selected, please try again..")
            time.sleep(0.5)

#Sub Menu Function                                  #Product                    products_list
def sub_menu(item_name, item_list):    #item_name <                 item_list <
    while True:                                     #Courier                    courier_list
        try:
            os.system('CLS')
            sm_options = int(input(f"""
                            {item_name} Menu:
                            0. Return to Main Menu
                            1. Print {item_name} List
                            2. Create a New {item_name}
                            3. Update {item_name} Details
                            4. Delete {item_name}
                            
                            Please Pick Required Menu Option: """))
            if sm_options in [0,1,2,3,4]:
                if sm_options == 0:
                    break
                elif sm_options == 1:
                    list_view(item_name, item_list)
                elif sm_options == 2:
                    new_item(item_name, item_list)
                elif sm_options == 3:
                    item_updt(item_name, item_list)
                elif sm_options == 4:
                    item_del(item_name, item_list)
            else:
                raise ValueError 
        except (TypeError, ValueError):
            print("\n Wrong option selected, please try again..")
            time.sleep(0.5)

#App Exit and save files Function
def save_and_exit():
    save_data(products_list, couriers_list)
    os.system('CLS')
    print("""   
                All files updated and saved.
                
                App is closing....""")
    time.sleep(1)
    exit()

#List View Function
def list_view(item_name, item_list):
    os.system('CLS')
    print(f"\n {item_name} List: {item_list}")
    input("\n Press 'Enter' to continue...")

#Adding Fuction
def new_item(item_name, item_list):
    while True:
        os.system('CLS')
        x = input(f"\n What is the name of the new {item_name}? ").lower().title()
        if x in item_list:
            print(f"\n {x} already exists. Please try again...")
            time.sleep(1)
        else:
            item_list.append(x) 
            print(f"\n {x} has been added.")
            print(f"\n New {item_name} list: {item_list}")
            menu_dec(item_name, item_list)
            break
            
#Updating Function
def item_updt(item_name, item_list):
    while True:
        try:
            os.system('CLS')
            for i in range(len(item_list)):
                print(f" Index [{i}] - {item_list[i]}")
            x = int(input(f"\n Which {item_name} would you like to update? Use {item_name} index value. "))
            if x in range(len(item_list)):
                while True:
                    y = input(f"\n What is the new {item_name} name? ").lower().title()      
                    if y in item_list:
                        print(f"\n {y} already exists.Please try again... ")
                    else:
                        os.system('CLS')
                        print(f"\n {item_list[x]} has been updated to {y} ")
                        item_list[x] = y
                        print(f"\n New {item_name} list: \n")
                        for i in range(len(item_list)):
                            print(f" Index [{i}] - {item_list[i]}")
                        menu_dec(item_name, item_list)
                        break
            else:
                raise ValueError
        except (TypeError, ValueError):
            print("\n Selected option doesn't meet required criteria, please try again..")
            time.sleep(0.5)

#Removing Function
def item_del(item_name, item_list):
    while True:
        os.system('CLS')
        print(f"\n {item_list}")
        z = input(f"\n Which {item_name} would you like to delete? ").lower().title()
        if z not in item_list:
            print(f"\n Chosen {item_name} not in the {item_list} list. Please try again...")
            time.sleep(0.5)
        else:
            decision = input(f"\n Are you sure you want to remove {z} ( y / n ): ")
            if decision == 'y':
                item_list.remove(z)
                print(f"\n {z} has been removed.")
                new_list = item_list
                print(f"\n New {item_name} list: {new_list}")
                menu_dec(item_name, item_list)
                break
            else:
                menu_dec(item_name, item_list)
                break

#Menu User Decison Fuction
def menu_dec(item_name, item_list):
    m_choice = input(f"\n Would you like to come back to the '{item_name} Menu'? (y/n) ").lower()
    if (m_choice != 'y' and m_choice != 'n'):
        print("\n Wrong option selected, please try again..")
        time.sleep(0.5)
        menu_dec(item_name, item_list)
    else:
        if m_choice == 'y':
            return
        else:
            main_menu()

main_menu()

