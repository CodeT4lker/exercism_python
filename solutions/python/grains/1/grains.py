def square(number):
    validate_input(number)
    return 2**(number - 1)


def total():
    tt = 0
    for i in range(1, 65):
        tt += 2**(i-1)
    return tt

def validate_input(number):
    if number < 1 or number > 64:
        raise ValueError('square must be between 1 and 64')
    