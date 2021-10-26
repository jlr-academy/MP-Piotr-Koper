from unittest.mock import patch, Mock, call
from src.utils import int_input_check, float_input_check
from src.utils import upper_case_conversion, task_choice

@patch('builtins.input')
def test_int_input_check(mock_input: Mock):
    # assemble
    expected = 5
    mock_input.return_value = '5'
        
    # act
    actual = int_input_check("Please provide integer")
    
    # assert
    assert expected == actual

@patch('builtins.print')
@patch('builtins.input')
def test_int_input_check_wrong_input(mock_input: Mock, mock_print: Mock):
    # assemble
    expected = "\n \tInvalid input. Please try again..."
    mock_input.side_effect = ['a', '1']
        
    # act
    int_input_check("Please provide integer")
    
    # assert
    mock_print.call_args_list[0] == call(expected)

@patch('builtins.input')
def test_int_input_check_empty_input(mock_input: Mock):
    # assemble
    expected = ""
    mock_input.return_value = ""

    # act
    actual = int_input_check("Please provide an integer number")

    # assert
    assert expected == actual

@patch('builtins.input')
def test_float_input_check(mock_input: Mock):
    # assemble
    expected = 5.0
    mock_input.return_value = '5'

    # act
    actual = float_input_check("Please provide a float number")
    
    # assert
    assert expected == actual

@patch('builtins.print')
@patch('builtins.input')
def test_float_input_check_wrong_input(mock_input: Mock, mock_print: Mock):
    # assemble
    expected = "\n \tInvalid input. Please try again..."
    mock_input.side_effect = ["a", "5.0"]
    
    # act
    float_input_check("Please provide a float number")
    
    # assert
    mock_print.call_args_list[0] = call(expected)

@patch('builtins.input')
def test_float_input_check_empty_input(mock_input: Mock):
    # assemble
    expected = ""
    mock_input.return_value = ""

    # act
    actual = float_input_check("Please provide a float number")
    
    # assert
    assert expected == actual

def test_upper_case_conversion():
    # assemble
    expected = "Hello World"
    string = "hello world"
    # act
    actual = upper_case_conversion(string)
    # assert
    assert expected == actual

@patch('builtins.input')
def test_task_choice_y(mock_input: Mock):
    # assemble
    expected = True
    mock_input. return_value = 'y'
    # act
    actual = task_choice("Would you like to continoue?")
    # assert
    assert expected == actual

@patch('builtins.input')
def test_task_choice_capital_y(mock_input: Mock):
    # assemble
    expected = True
    mock_input. return_value = 'Y'
    # act
    actual = task_choice("Would you like to continoue?")
    # assert
    assert expected == actual

@patch('builtins.input')
def test_task_choice_n(mock_input: Mock):
    # assemble
    expected = False
    mock_input. return_value = 'n'
    # act
    actual = task_choice("Would you like to continoue?")
    # assert
    assert expected == actual

@patch('builtins.input')
def test_task_choice_capital_n(mock_input: Mock):
    # assemble
    expected = False
    mock_input. return_value = 'N'
    # act
    actual = task_choice("Would you like to continoue?")
    # assert
    assert expected == actual

@patch('builtins.print')
@patch('builtins.input')
def test_task_choice_wrong_input(mock_input: Mock, mock_print: Mock):
    # assemble
    expected = "\n \tInvalid choice. Please try again..."
    mock_input.side_effect = ['a', 'y']
    # act
    task_choice("Would you like to continoue?")
    # assert
    mock_print.call_args_list[0] == call(expected)