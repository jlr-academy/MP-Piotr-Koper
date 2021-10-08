from main import new_item

def test_new_item():
    # assemble
    expected = 'Tea'
    product_list = ['Coke Zero', 'Pepsi Max', 'Coffee', 'Americano']
    
    def input(*args):
        return expected
    # act
    new_item('products',product_list, input)
    
    # assert
    if expected not in product_list:
        raise AssertionError

test_new_item()