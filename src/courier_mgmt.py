import os
from src.utils import sql_read, sql_execute, clear_screen
from src.utils import upper_case_conversion, task_choice
from src.utils import view_all_couriers, courier_id_check

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
        [4]. Delete courier""")
        choice = input("\tPlease pick a menu option: ")
        if choice == '0':
            break
        elif choice == '1':
            couriers_view()
        elif choice == '2':
            add_new_courier()
        elif choice == '3':
            courier_update()
        elif choice == '4':
            courier_delete()
        else:
            print("\n \tInvalid choice. Please try again...")

#Couerirs View from DB
def couriers_view():

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

def courier_update():
    
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
def courier_delete():
    task_check = True
    while task_check == True:
        id_choice = courier_id_check("\n \tPlease use Id value of the couirer you'd like to delete? ")
        sql = "DELETE FROM couriers WHERE courier_id=%s"
        sql_execute(sql, id_choice)
        task_check = task_choice("\n \tWould you like to delete another courier")