"""
Simple armstrong number checker
"""

def is_armstrong_number(number):
    original = number
    digits = str(number)
    length = len(digits)
    total = 0
    for digit in digits:
        total += int(digit) ** length
    return total == original
        
