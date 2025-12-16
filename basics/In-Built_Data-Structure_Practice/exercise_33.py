"""
Problem: Check if Tuple is Palindromic

Description:
    Design a Python function named is_palindromic_tuple to check if a tuple is 
    palindromic, meaning it reads the same forwards and backwards.

Input Parameters:
    tup (tuple): The input tuple to check.

Output:
    bool: True if the tuple is palindromic, False otherwise.

Examples:
    Input: (1, 2, 3, 2, 1)
    Output: True

    Input: (1, 2, 3, 4, 5)
    Output: False
"""

def is_palindromic_tuple(tup):
    n = len(tup)

    for i in range(n // 2):
        if tup[i] != tup[n - 1 - i]:
            return False 
            
    return True  

print(is_palindromic_tuple((1, 2, 3, 2, 1)))