def condition_transform(x, transform_function):
    try:
        transform_function(x)
        return True
    except:
        return False

def input_with_condition(input_function, condition, error_function):
    while True:
        inp = input_function()
        if condition(inp):
            return inp
        error_function(inp)
        
def input_with_transform(input_function, transform_function):
    return transform_function(input_function())