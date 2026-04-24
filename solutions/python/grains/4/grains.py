"""
Simple program to calculate the number of grains of wheat on a chessboard.

A chessboard has 64 squares. Square 1 has one grain, square 2 has two grains, square 3 has four grains, and so on, doubling each time.
"""

def square(number):
    validate_input(number)
    return 2**(number - 1)


def total():
    total_grains = 0
    for chess_square in range(1, 65):
        total_grains += 2**(chess_square - 1)
    return total_grains

def validate_input(number):
    if number < 1 or number > 64:
        raise ValueError('square must be between 1 and 64')
    