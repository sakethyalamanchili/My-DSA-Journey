"""
Problem: Is Array Sorted?

Description:
    Write a function that checks whether the given array is sorted in 
    non-decreasing order. The array is considered sorted if every element 
    is less than or equal to the next element.
    
    *Constraint:* You must iterate through the array to check the order. 
    Do not simply use "return arr == sorted(arr)" as that takes O(N log N) time.
    The goal is O(N) time.
    *Companies:* Google, Microsoft, Amazon, Facebook

Input Parameters:
    arr (List[int]): A list of integers.

Output:
    bool: True if the array is sorted, False otherwise.

Examples:
    Input: arr = [1, 2, 3, 4, 5]
    Output: True

    Input: arr = [5, 4, 3, 2, 1]
    Output: False

    Input: arr = [1, 3, 2, 4, 5]
    Output: False
"""

def is_sorted(arr):
    n = len(arr)
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            return False    
    return True

print(is_sorted(arr = [1, 2, 3, 4, 5]))
print(is_sorted(arr = [5, 4, 3, 2, 1]))
print(is_sorted(arr = [1, 3, 2, 4, 5]))
print(is_sorted(arr = [2, 10, 12, 80]))