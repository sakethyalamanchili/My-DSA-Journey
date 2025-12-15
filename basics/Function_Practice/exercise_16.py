"""
Problem: Celsius to Fahrenheit

Description:
    You are given a temperature in Celsius. Your task is to convert it to Fahrenheit 
    and return the result.

    Formula: F = (9/5 * C) + 32

Input Parameters:
    c (float): The temperature in Celsius.

Output:
    float: The temperature in Fahrenheit.

Examples:
    Input: 25
    Output: 77.0

    Input: 0
    Output: 32.0
"""

def celsius_to_fahrenheit(c):
    C = float(c)
    conversion = (((9 / 5) * C) + 32)
    return conversion

print(celsius_to_fahrenheit(21))