import json
from typing import List

def load_data(products_list: List, couriers_list: List, orders_list: List):
    try:
        with open('products.txt', 'r') as p_file:
            for line in p_file.readlines():
                products_list.append(line.strip())

        with open('couriers.txt', 'r') as c_file:
            for line in c_file.readlines():
                couriers_list.append(line.strip())

        with open('orders.json') as o_file:
            orders = json.load(o_file)
            orders_list.extend(orders)

    except FileNotFoundError as fnfd:
        print("File not found" + fnfd)
    except Exception as e:
        print("Something went wrong" + e)

def save_data(products_list: List, couriers_list: List, orders_list: List):
    try:
        with open('products.txt', 'w') as p_file:
            for item in products_list:
                p_file.write(item + '\n')

        with open('couriers.txt', 'w') as c_file:
            for item in couriers_list:
                c_file.write(item + '\n')

        with open('orders.json', 'w') as o_file:
                json.dump(orders_list, o_file)
                
    except Exception as e:
        print("Something went wrong:" + str(e))