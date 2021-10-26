from unittest.mock import patch, Mock, call
from app import main_menu


# @patch('builtins.print')
# @patch('builtins.input')
# def test_main_menu_first_option(mock_input: Mock, mock_print: Mock):
#     # assemble
#     expected = """
#         Product Menu:
#         ------------------------------
#         [0]. Return to Main Menu
#         [1]. View products
#         [2]. Create a new product
#         [3]. Update product details
#         [4]. Delete product"""
#     mock_input.side_effect = ['1', '0']
#     # act
#     main_menu()
#     # assert
#     mock_print.call_args_list[0] == call(expected)
    
@patch('app.product_menu')
@patch('builtins.input')
def test_main_menu_first_option(mock_input: Mock, mock_product_menu: Mock):
    # assemble
    mock_input.side_effect = ['1', 0]
    # act
    main_menu()
    # assert
    mock_product_menu.assert_called_once()

@patch('app.courier_menu')
@patch('builtins.input')
def test_main_menu_second_option(mock_input: Mock, mock_courier_menu: Mock):
    # assemble
    mock_input.side_effect = ['2', 0]
    # act
    main_menu()
    # assert
    mock_courier_menu.assert_called_once()

@patch('app.orders_menu')
@patch('builtins.input')
def test_main_menu_third_option(mock_input: Mock, mock_orders_menu: Mock):
    # assemble
    mock_input.side_effect = ['3', 0]
    # act
    main_menu()
    # assert
    mock_orders_menu.assert_called_once()

@patch('builtins.print')
@patch('builtins.input')
def test_main_menu_wrong_input(mock_input: Mock, mock_print: Mock):
    # assemble
    expected = "\n \tInvalid choice. Please try again..."
    mock_input.side_effect = ["a", 0]
    
    # act
    main_menu()
    
    # assert
    mock_print.call_args_list[0] = call(expected)
