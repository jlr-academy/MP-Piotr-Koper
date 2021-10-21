from app import add_new_item
from unittest.mock import patch, Mock, call

@patch('builtins.input')
def test_add_new_product(mock_input: Mock):
    # assemble
    expected = {'name': 'Americano', 'price': 1.3}
    product_list = [{'name': 'Coke Zero', 'price': '0.8'}, {'name': 'Pepsi', 'price': '1.2'}, {'name': 'Tea', 'price': '4.0'}]
    
    mock_input.side_effect = ["Americano", "1.3"]    
    
    # act
    add_new_item('product',product_list)

    # assert
    if expected not in product_list:
        raise AssertionError


@patch('builtins.print')
@patch('builtins.input')
def test_add_new_product_already_exist(mock_input: Mock, mock_print: Mock):
    #assemble
    product_list = [{'name': 'Coke Zero', 'price': '0.8'}, {'name': 'Pepsi', 'price': '1.2'}, {'name': 'Tea', 'price': '4.0'}]
    new_product = 'Coke Zero'
    expected = f"\t {new_product} already exists. Please try again..."
    mock_input.side_effect = [new_product, "Americano", "1.3"]
    #act
    add_new_item('product',product_list)
    #assert
    mock_print.call_args_list[0] == call(expected)
    

@patch('builtins.input')
def test_add_new_courier(mock_input: Mock):
    # assemble
    expected = {'name': 'Steve', 'phone': '111111'}
    courier_list = [{'name': 'Bob', 'phone': '0789887889'}, {'name': 'Joe', 'phone': '0789123456'}]
    
    mock_input.side_effect = ["Steve", "111111"]    
    
    # act
    add_new_item('courier',courier_list)
    
    # assert
    if expected not in courier_list:
        raise AssertionError