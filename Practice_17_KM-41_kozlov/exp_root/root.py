def root2(radicand):
    if not (isinstance(radicand, float) or isinstance(radicand, int)):
        raise ValueError("A radicand must be a float or an int")
    if radicand < 0:
        raise ValueError("A radicand must be non-negative")
    
    return radicand ** (1 / 2)

def root3(radicand):
    if not (isinstance(radicand, float) or isinstance(radicand, int)):
        raise ValueError("A radicand must be a float or an int")
    
    return radicand ** (1 / 3)