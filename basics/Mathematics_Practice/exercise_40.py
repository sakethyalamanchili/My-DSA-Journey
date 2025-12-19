"""
Problem: Decimal to Binary

Description:
    You are given an integer n. Your task is to return its binary representation 
    as a string. Do not use any built-in functions for conversion (like bin()).

Input Parameters:
    n (int): The integer to convert.

Output:
    str: The binary representation of n.

Examples:
    Input: n = 5
    Output: "101"

    Input: n = -5
    Output: "-101"
"""

def binary_to_decimal(n):
    if n == 0: return "0"
    
    is_negative = False
    
    if n < 0:
        is_negative = True
        n = abs(n)
        
    bits = []
    
    while n > 0:
        remainder = n % 2
        bits.append(str(remainder))
        n = n // 2
    
    result = "".join(bits[::-1])
    
    if is_negative == True:
        return "-" + result
    else:
        return result
    
print(binary_to_decimal(5))