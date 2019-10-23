def add_numbers(x, y):
    """ add two numbers and return the result"""
    return x+y

def subtract_numbers(x, y):
    if x > y:
        return x-y
    elif x<y:
        return y-x
    else:
        return 0