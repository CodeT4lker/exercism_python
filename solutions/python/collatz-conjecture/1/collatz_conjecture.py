"""
Given a positive integer, returns the number of steps it takes to reach 1 according to the rules of the Collatz Conjecture.
"""

def steps(number):
    validate_input(number)
    step_count = 0
    while number != 1:
        if number % 2 == 0:
            number //= 2
        else:
            number = number * 3 + 1
        step_count += 1
    return step_count

def validate_input(number):
    if not isinstance(number, int) or number < 1:
        raise ValueError("Only positive integers are allowed")