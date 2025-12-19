"""
Problem: Check for Even Number

Description:
    You are given an integer n. Your task is to check whether the number is even or not. 
    Return True if the number is even, and False otherwise.

Input Parameters:
    n (int): The integer to check.

Output:
    bool: True if n is even, False otherwise.

Examples:
    Input: n = 4
    Output: True

    Input: n = 7
    Output: False
"""

def is_even(n):
    if n % 2 == 0:
        return True
    return False

print(is_even(7))