"""
Problem: Check for Prime Number

Description:
    You are given an integer n. Your task is to check whether the number is prime 
    or not. A prime number is a number greater than 1 that has no divisors other 
    than 1 and itself.

Input Parameters:
    n (int): The integer to check.

Output:
    bool: True if n is a prime number, False otherwise.

Examples:
    Input: n = 5
    Output: True

    Input: n = 4
    Output: False
"""

def is_prime(n):
    if n <= 1: return False
    
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True

print(is_prime(4))