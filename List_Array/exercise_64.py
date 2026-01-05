"""
Problem: Maximum Element in a List (Manual Implementation)

Description:
    Given a list of integers, write a function to find the maximum element 
    in the list.
    
    *Constraint:* Try to implement this without using the built-in max() function 
    to understand the underlying logic.
    *Companies:* Google, Amazon, Microsoft, Facebook

Input Parameters:
    lst (List[int]): A list of integers (assume the list is non-empty).

Output:
    int: The maximum element in the list.

Examples:
    Input: lst = [3, 5, 2, 9, 6]
    Output: 9

    Input: lst = [-1, -2, -3, -4]
    Output: -1
"""

def find_max_element(lst):
    """
    Function to find the maximum element in a list.
    :param lst: List[int] -> List of integers
    :return: int -> The maximum element in the list
    """
    n = len(lst)
    max = lst[0]
    for i in range(n):
        if lst[i] > max:
            max = lst[i]
    return max

print(find_max_element(lst = [40, 50]))