"""
Problem: Line Equation

Description:
    You are given the slope (m) and the y-intercept (b) of a line, along with a value x. 
    Your task is to calculate and return the value of y using the equation of a line.

    Formula: y = (slope * x) + intercept

Input Parameters:
    slope (float): The slope of the line (m).
    intercept (float): The y-intercept of the line (b).
    x (float): The x-coordinate to solve for.

Output:
    float: The calculated y value.

Examples:
    Input: slope = 2, intercept = 3, x = 4
    Output: 11.0  (2 * 4 + 3 = 11)

    Input: slope = 1.5, intercept = -2, x = 2
    Output: 1.0   (1.5 * 2 + -2 = 1.0)
"""

def calculate_y(slope, intercept, x):
    slope = float(slope)
    intercept = float(intercept)
    x = float(x)
    
    y = (slope * x) + intercept
    
    return y

print(calculate_y(2, 3, 4))