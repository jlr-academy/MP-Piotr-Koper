# import builtins
# from app import list_view

# def test_list_view():
#     #assemble
#     result = """
#         Product list:
#         ------------------------------------
#         [0] - {'0.8', 'Coke Zero'}
#         [1] - {'1.2', 'Pepsi'}
#         [2] - {'4.0', 'Tea'}"""
        
#     item_name = 'product'
#     product_list = [{'name': 'Coke Zero', 'price': '0.8'}, {'name': 'Pepsi', 'price': '1.2'}, {'name': 'Tea', 'price': '4.0'}]
#     #act
#     actual = list_view(item_name, product_list)
    
#     #assert
#     assert result == actual