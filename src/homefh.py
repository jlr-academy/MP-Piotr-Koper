import os
import json
from typing import List

def load_data(item_name: str):
    
    item_list = []
    
    if item_name == 'orders':
        path = f"..\data\{item_name}.json"
        try:
            with open(os.path.join(os.path.dirname(__file__), path), 'r') as file:
                orders = json.load(file)
                item_list.extend(orders)
        except FileNotFoundError as fnfd:
            print("File not found" + str(fnfd))
        except Exception as e:
            print("Something went wrong" + str(e))
    else:
        path = f"..\data\{item_name}.txt"
        try:
            with open(os.path.join(os.path.dirname(__file__), path), 'r') as file:
                for line in file.readlines():
                    item_list.append(line.strip())
        except FileNotFoundError as fnfd:
            print("File not found" + str(fnfd))
        except Exception as e:
            print("Something went wrong" + str(e))

    return item_list


def save_data(item_name, item_list):
    
    if item_name == 'orders':
        path = f"..\data\{item_name}.json"
        try:
            with open(os.path.join(os.path.dirname(__file__), path), 'r') as file:
                json.dump(item_list, file)
        except Exception as e:
            print("Something went wrong:" + str(e))
    else:
        path = f"..\data\{item_name}.txt"
        try:
            with open(os.path.join(os.path.dirname(__file__), path), 'w') as file:
                for item in item_list:
                    file.write(item + '\n')        
        except Exception as e:
            print("Something went wrong:" + str(e))