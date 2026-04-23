"""
Simple program to determine if a triangle is equilateral, isosceles, or scalene.
"""

def equilateral(sides):
    if is_triangle(sides) == False:
        return False
    elif sides[0] == sides[1] and sides[2] == sides[0]:
        return True
    return False


def isosceles(sides):
    if is_triangle(sides) == False:
        return False
    return (sides[0] == sides[1] or
           sides[0] == sides[2] or
           sides[1] == sides[2]) 


def scalene(sides):
    if is_triangle(sides) == False:
        return False
    if sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]:
        return False
    return True

def is_triangle(sides):
    if sides[0] <= 0.0 or sides[1] <= 0.0 or sides[2] <= 0.0:
        return False
    if (sides[0] + sides[1] <= sides[2] or
        sides[0] + sides[2] <= sides[1] or
        sides[1] + sides[2] <= sides[0]):
        return False
    return True
        