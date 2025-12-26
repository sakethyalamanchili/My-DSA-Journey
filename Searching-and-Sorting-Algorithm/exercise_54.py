"""
Problem: Linear Search in a List

Description:
    Implement a function linear_search that performs a linear search on a list 
    to find a given value. The function should return the index of the first 
    occurrence of the value in the list, or -1 if the value is not found.

Input Parameters:
    arr (list): A list of elements (can be empty).
    target (any): The value to search for in the list.

Output:
    int: The index of the first occurrence of the target value (0-based), 
         or -1 if not found.

Examples:
    Input: arr = [3, 7, 2, 5], target = 2
    Output: 2

    Input: arr = [1, 1, 2, 1], target = 1
    Output: 0
    
    Input: arr = [4, 2, 8], target = 6
    Output: -1
"""

def linear_search(arr, target):
    for i in range(len(arr)):
        if target == arr[i]:
            return i
    return -1

print(linear_search(arr = [1, 1, 2, 1], target = 1))