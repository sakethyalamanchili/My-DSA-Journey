"""
Problem: Binary to Decimal

Description:
    You are given a string binary_str representing a binary number. Your task is to 
    convert this binary string to its corresponding decimal integer. 
    Do not use any built-in functions for conversion (like int(s, 2)).

Input Parameters:
    binary_str (str): A string consisting of '0' and '1'.

Output:
    int: The decimal integer value of the binary string.

Examples:
    Input: binary_str = "101"
    Output: 5

    Input: binary_str = "1101"
    Output: 13
"""

def binary_to_decimal(binary_str):
    total = 0
    length = len(binary_str)
    
    for i in range(length):
        digit = binary_str[length - 1 - i]
        
        if digit == '1':
            total += 2 ** i
            
    return total

print(binary_to_decimal("1101")) 