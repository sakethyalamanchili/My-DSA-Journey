"""
Problem: Remove Duplicates from a List

Description:
    You are given a list of integers. Write a Python program that removes any duplicate 
    elements from the list and returns a new list with only unique elements. 
    The order of elements should be maintained.

    *Constraint:* Do not use the set() function. Use brute force logic.

Input Parameters:
    lst (List[int]): The list of integers to process.

Output:
    List[int]: A list of integers with duplicates removed, preserving order.

Examples:
    Input: lst = [1, 2, 2, 3, 4, 4, 5]
    Output: [1, 2, 3, 4, 5]

    Input: lst = [4, 5, 5, 4, 6, 7]
    Output: [4, 5, 6, 7]
"""

def remove_duplicates(lst):
    empty_list = []
    for i, num in enumerate(lst):
        if num not in empty_list:
            empty_list.append(num)
    
    return empty_list
            
print(remove_duplicates([4, 5, 5, 4, 6, 7]))