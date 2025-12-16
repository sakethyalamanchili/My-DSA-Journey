"""
Problem: Check if All Elements in a List are Unique

Description:
    You are given a list of integers. Write a Python program that checks if all 
    elements in the list are unique. 
    If all elements are unique, return True; otherwise, return False.

Input Parameters:
    lst (List[int]): The list of integers to check.

Output:
    bool: True if all elements are unique, False otherwise.

Examples:
    Input: lst = [1, 2, 3, 4, 5]
    Output: True

    Input: lst = [1, 2, 3, 3, 4, 5]
    Output: False
"""

def check_unique(lst):
    empty_list = []
    for i, num in enumerate(lst):
        if num not in empty_list:
            empty_list.append(num)
    if empty_list == lst:
        return True
    return False

print(check_unique([1, 2, 3, 4, 5]))        