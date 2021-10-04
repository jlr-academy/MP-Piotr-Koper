
import os
import time

try:
    products = []
    with open('products.txt', 'r') as p_file:
        for line in p_file.readlines():
            products.append(line.strip())

    couriers = []
    with open('couriers.txt', 'r') as c_file:
        for line in c_file.readlines():
            couriers.append(line.strip())
except FileNotFoundError as fnfd:
    print("File not found" + fnfd)
except Exception as e:
    print("Something went wrong" + e)

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
                    app_exit()
                    # break                               
                elif mm_options == 1:
                    sub_menu("Product", products)
                elif mm_options == 2:
                    sub_menu("Courier", couriers)
            else:
                raise ValueError 
        except (TypeError, ValueError):
            print("\n Wrong option selected, please try again..")
            time.sleep(0.5)

#Sub Menu Function
def sub_menu(item_name, item_list):
    while True:
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
def app_exit():
    try:
        with open('products.txt', 'w') as p_file:
            for item in products:
                p_file.write(item + '\n')
        with open('couriers.txt', 'w') as c_file:
            for item in couriers:
                c_file.write(item + '\n')
    except Exception as e:
        print("Something went wrong:" + str(e))
    os.system('CLS')
    print("""   All files updated and saved.
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
        x = input(f"\n What is the item_name of the new {item_name}? ").lower().title()
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
        os.system('CLS')
        for i in range(len(item_list)):
            print(f" Index [{i}] - {item_list[i]}")
        x = int(input(f"\n Which {item_name} would you like to update? Use {item_name} index value. "))   #Add error handling if item_name used rather index
        if x > len(item_list)-1:
            print("\n Selected index value out of range. Please try again...\n ")
            time.sleep(1)
        else:
            while True:
                y = input(f"\n What is the new {item_name} item_name? ").lower().title()      
                if y in item_list:
                    print(f"\n {y} already exists.Please try again... ")
                else:
                    print(f"\n The item_name for the {item_name}: {item_list[x]} has been updated to: {y} ")
                    item_list[x] = y
                    new_list = item_list                                                                   
                    print(f"\n New {item_name} list: {new_list}")
                    menu_dec(item_name, item_list)
                    break
            break

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
            else:
                menu_dec(item_name, item_list)

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
            app_exit()

main_menu()

