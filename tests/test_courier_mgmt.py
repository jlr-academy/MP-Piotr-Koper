from unittest.mock import patch, Mock, call
from src.courier_mgmt import courier_menu

@patch('src.courier_mgmt.view_couriers')
@patch('builtins.input')
def test_courier_menu_first_option(mock_input: Mock, mock_view_couriers: Mock):
    # assemble
    mock_input.side_effect = ['1', 0]
    # act
    courier_menu()
    # assert
    mock_view_couriers.assert_called_once()

@patch('src.courier_mgmt.add_new_courier')
@patch('builtins.input')
def test_courier_menu_second_option(mock_input: Mock, mock_add_new_courier: Mock):
    # assemble
    mock_input.side_effect = ['2', 0]
    # act
    courier_menu()
    # assert
    mock_add_new_courier.assert_called_once()

@patch('src.courier_mgmt.update_courier')
@patch('builtins.input')
def test_courier_menu_third_option(mock_input: Mock, mock_update_courier: Mock):
    # assemble
    mock_input.side_effect = ['3', 0]
    # act
    courier_menu()
    # assert
    mock_update_courier.assert_called_once()

@patch('src.courier_mgmt.delete_courier')
@patch('builtins.input')
def test_courier_menu_fourth_option(mock_input: Mock, mock_delete_courier: Mock):
    # assemble
    mock_input.side_effect = ['4', 0]
    # act
    courier_menu()
    # assert
    mock_delete_courier.assert_called_once()

@patch('builtins.print')
@patch('builtins.input')
def test_courier_menu_wrong_input(mock_input: Mock, mock_print: Mock):
    # assemble
    expected = "\n \tInvalid choice. Please try again..."
    mock_input.side_effect = ["a", 0]
    
    # act
    courier_menu()
    
    # assert
    mock_print.call_args_list[0] = call(expected)
