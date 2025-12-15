"""
Problem: Area of a Rectangle

Description:
    You are given the length and breadth of a rectangle. Your task is to compute 
    and return the area of the rectangle.

    Formula: Area = length * breadth

Input Parameters:
    length (float): The length of the rectangle.
    breadth (float): The breadth (width) of the rectangle.

Output:
    float: The calculated area of the rectangle.

Examples:
    Input: length = 5, breadth = 3
    Output: 15.0

    Input: length = 7.5, breadth = 2.4
    Output: 18.0
"""

def area_of_rectangle(length, breadth):
    L = float(length)
    B = float(breadth)
    conversion = L * B
    return conversion

print(area_of_rectangle(5, 3))