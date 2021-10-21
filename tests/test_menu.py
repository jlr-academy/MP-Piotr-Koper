import builtins
from app import pc_menu
from unittest.mock import Mock, patch
from app import main_menu

@patch("app.list_view")
@patch("builtins.input")
def test_pc_menu(mock_input: Mock, mock_list_view: Mock):
    #assemble    
    dummy_item_name = 'product'
    dummy_item_list = ["Tea", "Pepsi"]
    mock_input.side_effect = ["1", "0"]
    #act
    pc_menu(dummy_item_name, dummy_item_list)
    #assert
    mock_list_view.assert_called_once()

# @patch("builtins.print")
# @patch("builtins.input")    
# def test_main_menu(mock_input: Mock, mock_print: Mock):
#     #assemle
#     expected = """
#         Product Menu:
#         ------------------------------
#         [0]. Return to Main Menu
#         [1]. View products list
#         [2]. Create a new product
#         [3]. Update product details
#         [4]. Delete product"""
        
#     item_name = 'product'
#     product_list = ["Tea", "Pepsi"]
#     mock_input.side_effect = ["1", "0"]
#     #act
#     main_menu("products_list", "couriers_list", "orders_list", "order_status_list")
#     #assert
#     # assert actual == expected
#     mock_print.assert_called_with(expected)