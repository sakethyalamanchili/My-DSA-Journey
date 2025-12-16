"""
Problem: Largest Element in a List

Description:
    Write a Python function that finds and returns the largest element in a given list of integers.

Input Parameters:
    numbers (List[int]): The input list containing integers.

Output:
    int: An integer representing the largest element in the input list.

Examples:
    Input: numbers = [3, 8, 2, 10, 5]
    Output: 10

    Input: numbers = [-5, -10, -2, -1, -7]
    Output: -1
"""

def find_largest(numbers):
    result = max(numbers)
    return result

print(find_largest([3, 8, 2, 10, 5]))