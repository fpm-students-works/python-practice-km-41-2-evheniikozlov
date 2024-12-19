def fact(argument):
    if not isinstance(argument, int):
        raise ValueError("An argument must be an int")
    if argument < 0:
        raise ValueError("An argument must be non-negative")
    
    result = 1
    for multiplier in range(2, argument + 1):
        result *= multiplier
    return result