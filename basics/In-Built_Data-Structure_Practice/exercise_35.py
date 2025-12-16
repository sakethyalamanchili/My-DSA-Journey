"""
Problem: Check if a List is a Subset of Another List (Brute Force)

Description:
    You are given two lists of integers. Write a Python program that checks whether 
    the first list is a subset of the second list using a brute-force approach, 
    without using the 'in' keyword. 
    
    A list is considered a subset if all elements of the first list are present 
    in the second list.

Input Parameters:
    lst1 (List[int]): The potential subset.
    lst2 (List[int]): The superset to check against.

Output:
    bool: True if lst1 is a subset of lst2, otherwise False.

Examples:
    Input: lst1 = [1, 2, 3], lst2 = [1, 2, 3, 4, 5]
    Output: True

    Input: lst1 = [1, 6], lst2 = [1, 2, 3, 4, 5]
    Output: False
"""

def is_subset(lst1, lst2):
    empty = []
    for i in lst1:
        for j in lst2:
            if i == j:
                empty.append(i)
    
    if empty == lst1:
        return True
    return False

print(is_subset(lst1 = [1, 6], lst2 = [1, 2, 3, 4, 5]))