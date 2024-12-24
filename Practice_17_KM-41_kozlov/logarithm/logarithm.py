from math import log as math_log, e

def log(base, argument):
    if not ((isinstance(base, float) or isinstance(base, int)) or (isinstance(argument, float) or isinstance(argument, int))):
        raise ValueError("A base and an argument must be a float or an int")
    if not (base > 0 and argument > 0):
        raise ValueError("A base and an argument must be positive")
    if base == 1:
        raise ValueError("A base can't equal 1")
    
    return math_log(argument, base)

def ln(argument):
    return log(e, argument)

def lg(argument):
    return log(10, argument)
