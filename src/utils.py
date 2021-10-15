import os
import time

def index_view(item_name, item_list):
    print(f"""
        {item_name.title()} list:
        ------------------------------------""")
    for index, name in enumerate(item_list):
        print(f"\t[{index}] - {name}")
    print("")
        

def does_index_exist(products_list, o_items):
    for idx in o_items:
        try:
            products_list[idx]
        except (IndexError, ValueError):
            return False
    return True

def user_idx_choice_check(item_name, item_list, task):
    while True:
        try:
            os.system('cls')
            index_view(item_name, item_list)
            idx_choice = int(input(f"\tPlease use index value for {item_name} details to be {task}. "))
            if idx_choice in range(len(item_list)):
                return idx_choice
            else:
                raise ValueError
        except ValueError:
            print("")
            print("\tInvalid choice. Please try again...")
            time.sleep(0.5)

def end_of_task_choice(item_name, task):
    os.system('cls')
    user_choice = input(f" Would you like to {task} another {item_name}? [y / n] ")
    if user_choice == 'y':
        pass
    elif user_choice == 'n':
        return False
    else:
        print("")
        print("\ttInvalid choice. Please try again...")