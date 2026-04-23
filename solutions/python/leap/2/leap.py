"""
Simple function to determin leap years.
"""

def leap_year(year):
    if (year % 4 == 0 and year % 100 != 00 )or year % 400 == 0:
        return True
    return False
