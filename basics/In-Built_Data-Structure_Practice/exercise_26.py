"""
Problem: Count Even and Odd Numbers in a List

Description:
    You are given a list of integers. Write a Python program that counts and returns 
    the number of even and odd numbers in the list.

Input Parameters:
    lst (List[int]): The list of integers to analyze.

Output:
    tuple: A tuple (even_count, odd_count) representing the count of 
    even and odd numbers respectively.

Examples:
    Input: lst = [1, 2, 3, 4, 5]
    Output: (2, 3)
    # Evens: 2, 4 (Total 2)
    # Odds: 1, 3, 5 (Total 3)
"""

def count_even_odd(lst):
    odd = []
    even = []
    
    for i, num in enumerate(lst):
        if num % 2 == 1:
            odd.append(num)
        else:
            even.append(num)
    
    odd_count = len(odd)
    even_count = len(even)
    result = (even_count, odd_count)
    
    return result

print(count_even_odd([1, 2, 3, 4, 5]))