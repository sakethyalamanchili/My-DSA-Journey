"""
Problem: Valid Perfect Square

Description:
    You are given a positive integer num. Your task is to check whether num is a 
    perfect square or not. A perfect square is an integer that is the square of 
    an integer (e.g., 1, 4, 9, 16).

Input Parameters:
    num (int): The positive integer to check.

Output:
    bool: True if num is a perfect square, False otherwise.

Examples:
    Input: num = 16
    Output: True   (4 * 4 = 16)

    Input: num = 14
    Output: False
"""

def is_perfect_square(num):
    if num < 1: 
        return False

    root = num ** 0.5

    return root.is_integer()

print(is_perfect_square(16)) # True
print(is_perfect_square(14)) # False