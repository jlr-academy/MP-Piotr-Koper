
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