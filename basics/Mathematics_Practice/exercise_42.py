"""
Problem: GCD of Two Numbers

Description:
    You are given two integers n and m. Your task is to find the Greatest Common 
    Divisor (GCD) of these two numbers. 
    The GCD is the largest positive integer that divides both numbers without 
    leaving a remainder.
    
    *Constraint:* Do not use built-in functions or recursion.

Input Parameters:
    n (int): The first integer.
    m (int): The second integer.

Output:
    int: The GCD of n and m.

Examples:
    Input: n = 48, m = 18
    Output: 6

    Input: n = 56, m = 98
    Output: 14
"""

def gcd(n, m):
    common_arr = []

    limit = min(n, m) + 1
    
    for i in range(1, limit):
        if (n % i == 0) and (m % i == 0):
            common_arr.append(i)

    return max(common_arr)

print(gcd(48, 18)) 