
def load_data(product_lists, couriers_list):
    try:
        with open('products.txt', 'r') as p_file:
            for line in p_file.readlines():
                product_lists.append(line.strip())

        with open('couriers.txt', 'r') as c_file:
            for line in c_file.readlines():
                couriers_list.append(line.strip())

    except FileNotFoundError as fnfd:
        print("File not found" + fnfd)
    except Exception as e:
        print("Something went wrong" + e)

def save_data(products_list, couriers_list):
    try:
        with open('products.txt', 'w') as p_file:
            for item in products_list:
                p_file.write(item + '\n')
        with open('couriers.txt', 'w') as c_file:
            for item in couriers_list:
                c_file.write(item + '\n')
    except Exception as e:
        print("Something went wrong:" + str(e))