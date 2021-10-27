import os
import csv

from src.utils import sql_read

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


def save_data(item_name: str):

    path = f"..\data\{item_name}.csv"
    
    if item_name == "products":
        sql = """  SELECT 'Id', 'Name', 'Price', 'Stock'
                    UNION ALL 
                    SELECT product_id, name, price, stock FROM products"""
        rows = sql_read(sql)
        with open(os.path.join(os.path.dirname(__file__), path), 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
            file.close()

    if item_name == "couriers":
        sql = """  SELECT 'Id', 'Name', 'Phone'
                    UNION ALL
                    SELECT courier_id, name, phone FROM couriers"""
        rows = sql_read(sql)
        with open(os.path.join(os.path.dirname(__file__), path), 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
            file.close()
    
    elif item_name == "orders":
        sql = """ SELECT 'Id', 'Customer Name', 'Customer Address', 'Customer Phone', 'Courier Id', 'Order Status', 'Product Id', 'Quantity'
                    UNION ALL
                    SELECT orders.order_id, customers.customer_name, customers.customer_address, customers.customer_phone, 
                    couriers.courier_id, order_status.order_status, IFNULL(orders_products.product_id, 0) AS product_id, IFNULL(orders_products.quantity, 0) AS quantity
                    FROM orders
                    LEFT JOIN customers
                    ON orders.customer_id = customers.customer_id
                    LEFT JOIN couriers
                    ON orders.courier_id = couriers.courier_id
                    LEFT JOIN order_status
                    ON orders.status_id = order_status.status_id
                    LEFT JOIN orders_products
                    ON orders.order_id = orders_products.order_id"""
        rows = sql_read(sql)
        with open(os.path.join(os.path.dirname(__file__), path), 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
            file.close()