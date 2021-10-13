import os
from typing import List
import csv

def load_data(item_name: str):

    item_list = []
    path = f"..\data\{item_name}.csv"

    try:

        with open(os.path.join(os.path.dirname(__file__), path), 'r') as file:
            reader = csv.DictReader(file)
            items = list(reader)
            item_list.extend(items)

    except FileNotFoundError as fnfd:
        print("File not found" + str(fnfd))
    except Exception as e:
        print("Something went wrong" + str(e))

    return item_list


def save_data(item_name: str, item_list: List):

    path = f"..\data\{item_name}.csv"
    
    if item_name == "products":
        header = ["name", "price"]
    elif item_name == "couriers":
        header = ["name", "phone"]
    elif item_name == "orders":
        header = ["customer_name", "customer_address", "customer_phone", "courier", "status", "items"]

    try:
        
        with open(os.path.join(os.path.dirname(__file__), path), 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames = header)
            writer.writeheader()
            writer.writerows(item_list)
            
    except Exception as e:
        print("Something went wrong:" + str(e))