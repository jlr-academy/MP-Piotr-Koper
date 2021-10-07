import os
import json
from typing import List

def load_data(products_list: List, couriers_list: List, orders_list: List):
    try:
        with open('C:\\Users\\pkoper\\Infinity_Works_JLR_Training\\miniproject\\data\\products.txt', 'r') as p_file:
            for line in p_file.readlines():
                products_list.append(line.strip())

        with open('C:\\Users\\pkoper\\Infinity_Works_JLR_Training\\miniproject\\data\\couriers.txt', 'r') as c_file:
            for line in c_file.readlines():
                couriers_list.append(line.strip())

        with open('C:\\Users\\pkoper\\Infinity_Works_JLR_Training\\miniproject\\data\\orders.json') as o_file:
            orders = json.load(o_file)
            orders_list.extend(orders)

    except FileNotFoundError as fnfd:
        print("File not found" + str(fnfd))
    except Exception as e:
        print("Something went wrong" + str(e))

def save_data(products_list: List, couriers_list: List, orders_list: List):
    try:
        with open('C:\\Users\\pkoper\\Infinity_Works_JLR_Training\\miniproject\\data\\products.txt', 'w') as p_file:
            for item in products_list:
                p_file.write(item + '\n')

        with open('C:\\Users\\pkoper\\Infinity_Works_JLR_Training\\miniproject\\data\\couriers.txt', 'w') as c_file:
            for item in couriers_list:
                c_file.write(item + '\n')

        with open('C:\\Users\\pkoper\\Infinity_Works_JLR_Training\\miniproject\\data\\orders.json', 'w') as o_file:
                json.dump(orders_list, o_file)
                
    except Exception as e:
        print("Something went wrong:" + str(e))