import os
from utils import clear_screen, couriers_view_all, upper_case_conversion
from utils import task_choice, courier_id_check

#Products & Couriers Menu Function - COMPLETE
def courier_menu(connection, cursor):

    choice = ""
    while choice != 0:
        clear_screen()
        print(f"""
        Courier Menu:
        ------------------------------
        [0]. Return to Main Menu
        [1]. View couriers list
        [2]. Create a new courier
        [3]. Update courier details
        [4]. Delete courier""")
        choice = input("\tPlease pick a menu option: ")
        if choice == '0':
            break
        elif choice == '1':
            couriers_view(cursor)
        elif choice == '2':
            add_new_courier(connection, cursor)
        elif choice == '3':
            courier_update(connection, cursor)
        elif choice == '4':
            courier_delete(connection, cursor)
        else:
            print("\n \tInvalid choice. Please try again...")

#Products View from DB
def couriers_view(cursor):

    clear_screen()
    couriers_view_all(cursor)
    os.system('pause')

#Adding New Courier to DB
def add_new_courier(connection, cursor):
    task_check = True
    while task_check == True:
        clear_screen()
        name = upper_case_conversion(input("\n \tWhat is the new courier name? "))
        phone = input(f"\n \tWhat is courier's phone number? ")
        cursor.execute("INSERT INTO couriers (name, phone) VALUES(%s, %s)",(name, phone))
        connection.commit()
        print(f"\n \t{name} with phone no. {phone} has beed added to the database")
        task_check = task_choice("\n \tWould you like to add another courier [y / n] ")

def courier_update(connection, cursor):
    task_check = True
    while task_check == True:
        clear_screen()
        couriers_view_all(cursor)
        id_choice = courier_id_check(cursor, "\n \tPlease use Id value for the courier you'd like to update? ")
        cursor.execute("SELECT courier_id, name, phone FROM couriers WHERE courier_id=%s",(id_choice))
        rows = cursor.fetchall()
        update_task_check = True
        while update_task_check == True:
            clear_screen()
            for row in rows:
                print(f"\t[1]. - Name: {str(row[1])}")
                print(f"\t[2]. - Phone: {row[2]}")
            el_choice = input("\n \tPlease use index value of the element you'd like to update? ")
            if el_choice == '1':
                name = input("\n \t What is courier's new name? ")
                if name == "":
                    pass
                else:
                    cursor.execute("UPDATE couriers SET name=%s WHERE courier_id=%s",(name, id_choice))
                    connection.commit()
            elif el_choice == '2':
                phone = input("\n \tWhat is courier's new phone number? ")
                if phone == "":
                    pass
                else:
                    cursor.execute("UPDATE couriers SET phone=%s WHERE courier_id=%s",(phone, id_choice))
                    connection.commit()
            else:
                print("\n \tInvalid input. Please try again...")
                continue
            update_task_check = task_choice("\n \tWould you like to update another element? [y / n] ")
        task_check = task_choice("\n \tWould you like to update another courier? [y / n] ")

#Deleteting Product from DB
def courier_delete(connection, cursor):
    task_check = True
    while task_check == True:
        clear_screen()
        couriers_view_all(cursor)
        id_choice = courier_id_check(cursor, "\n \tPlease use Id value of the couirer you'd like to delete? ")
        cursor.execute("DELETE FROM couriers WHERE courier_id=%s", (id_choice))
        connection.commit()
        task_check = task_choice("\n \tWould you like to delete another courier")