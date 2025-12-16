"""
Problem: Sum of List Elements

Description:
    Write a Python function that calculates the sum of all elements in a given list of integers.

Input Parameters:
    numbers (List[int]): The input list containing integers.

Output:
    int: An integer representing the sum of all elements in the input list.

Examples:
    Input: numbers = [1, 2, 3, 4, 5]
    Output: 15

    Input: numbers = [10, -5, 7, 8, -2]
    Output: 18
"""

def sum_list(numbers):
    result = sum(numbers)
    return result

print(sum_list([1, 2, 3, 4, 5]))