from unittest.mock import patch, Mock, call
from src.customer_mgmt import customer_menu

@patch('src.customer_mgmt.view_customers')
@patch('builtins.input')
def test_product_menu_first_option(mock_input: Mock, mock_view_customers: Mock):
    # assemble
    mock_input.side_effect = ['1', 0]
    # act
    customer_menu()
    # assert
    mock_view_customers.assert_called_once()

@patch('src.customer_mgmt.add_new_customer')
@patch('builtins.input')
def test_product_menu_second_option(mock_input: Mock, mock_add_new_customer: Mock):
    # assemble
    mock_input.side_effect = ['2', 0]
    # act
    customer_menu()
    # assert
    mock_add_new_customer.assert_called_once()

@patch('src.customer_mgmt.update_customer')
@patch('builtins.input')
def test_product_menu_third_option(mock_input: Mock, mock_update_customer: Mock):
    # assemble
    mock_input.side_effect = ['3', 0]
    # act
    customer_menu()
    # assert
    mock_update_customer.assert_called_once()

@patch('src.customer_mgmt.delete_customer')
@patch('builtins.input')
def test_product_menu_fourth_option(mock_input: Mock, mock_delete_customer: Mock):
    # assemble
    mock_input.side_effect = ['4', 0]
    # act
    customer_menu()
    # assert
    mock_delete_customer.assert_called_once()

@patch('builtins.print')
@patch('builtins.input')
def test_product_menu_wrong_input(mock_input: Mock, mock_print: Mock):
    # assemble
    expected = "\n \tInvalid choice. Please try again..."
    mock_input.side_effect = ["a", 0]
    
    # act
    customer_menu()
    
    # assert
    mock_print.call_args_list[0] = call(expected)
