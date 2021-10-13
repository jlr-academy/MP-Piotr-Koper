
def index_view(item_name, item_list):
    print(f"""
        {item_name.title()} list:
        ------------------------------------""")
    for index, name in enumerate(item_list):
        print(f"\t[{index}] - {name}")
    print("")
        