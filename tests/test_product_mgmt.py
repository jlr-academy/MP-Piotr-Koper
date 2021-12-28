from unittest.mock import patch, Mock, call
from src.product_mgmt import product_menu

@patch('src.product_mgmt.view_products')
@patch('builtins.input')
def test_product_menu_first_option(mock_input: Mock, mock_view_products: Mock):
    # assemble
    mock_input.side_effect = ['1', 0]
    # act
    product_menu()
    # assert
    mock_view_products.assert_called_once()

@patch('src.product_mgmt.add_new_product')
@patch('builtins.input')
def test_product_menu_second_option(mock_input: Mock, mock_add_new_product: Mock):
    # assemble
    mock_input.side_effect = ['2', 0]
    # act
    product_menu()
    # assert
    mock_add_new_product.assert_called_once()

@patch('src.product_mgmt.update_product')
@patch('builtins.input')
def test_product_menu_third_option(mock_input: Mock, mock_update_product: Mock):
    # assemble
    mock_input.side_effect = ['3', 0]
    # act
    product_menu()
    # assert
    mock_update_product.assert_called_once()

@patch('src.product_mgmt.delete_product')
@patch('builtins.input')
def test_product_menu_fourth_option(mock_input: Mock, mock_delete_product: Mock):
    # assemble
    mock_input.side_effect = ['4', 0]
    # act
    product_menu()
    # assert
    mock_delete_product.assert_called_once()

@patch('builtins.print')
@patch('builtins.input')
def test_product_menu_wrong_input(mock_input: Mock, mock_print: Mock):
    # assemble
    expected = "\n \tInvalid choice. Please try again..."
    mock_input.side_effect = ["a", 0]
    
    # act
    product_menu()
    
    # assert
    mock_print.call_args_list[0] = call(expected)
