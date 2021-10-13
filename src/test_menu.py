import builtins
from home import pc_menu
from unittest.mock import Mock, patch

@patch("home.list_view")
@patch("builtins.input")
@patch("builtins.print")
def test_pc_menu(mock_print: Mock, mock_input: Mock, mock_list_view: Mock):
    #assemble
    expected_response = "Product Menu:"
    "------------------------------"
    "[0]. Return to Main Menu"
    "[1]. View products list"
    "[2]. Create a new product"
    "[3]. Update product details"
    "[4]. Delete product"
        
    dummy_item_name = 'product'
    dummy_item_list = ["Tea", "Pepsi"]
    mock_input.side_effect = ["1", "0"]
    #act
    pc_menu(dummy_item_name, dummy_item_list)
    #assert
    mock_list_view.assert_called_once()
    # assert actual == expected_response