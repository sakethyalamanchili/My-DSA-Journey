"""
Problem: Binary Search in a Sorted List

Description:
    Implement a function binary_search that performs a binary search on a 
    sorted list to find a given value. The function should return the index of 
    the value in the list, or -1 if the value is not found.

    *Constraint:* The input list 'arr' is guaranteed to be sorted in ascending order.

Input Parameters:
    arr (list): A sorted list of integers.
    target (int): The value to search for.

Output:
    int: The index of the target value (0-based), or -1 if not found.

Examples:
    Input: arr = [1, 2, 3, 4, 5, 6, 7], target = 5
    Output: 4

    Input: arr = [10, 20, 30, 40, 50], target = 25
    Output: -1
"""

def binary_search(arr, target):
    # arr.sort() (Input is already guaranteed to be sorted)
    start = 0
    end = len(arr) - 1
    
    while start <= end:
        middle = (start + end) // 2
        if target == arr[middle]:
            return middle
        elif target > arr[middle]:
            start = middle + 1
        elif target < arr[middle]:
            end = middle - 1
    return -1

print(binary_search(arr = [1, 2, 3, 4, 5, 6, 7], target = 5))