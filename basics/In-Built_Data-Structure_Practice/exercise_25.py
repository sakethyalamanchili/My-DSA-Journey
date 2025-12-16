"""
Problem: Reverse a List (Non-Slicing Approach)

Description:
    You are given a list of integers. Write a Python program that reverses the list 
    without using slicing (lst[::-1]). The program should return the reversed list.

Input Parameters:
    lst (List[int]): The list of integers to be reversed.

Output:
    List[int]: A new list with elements in reverse order.

Examples:
    Input: lst = [1, 2, 3, 4, 5]
    Output: [5, 4, 3, 2, 1]
"""

def reverse_list(lst):
    empty_list = []
    n = (len(lst) - 1)
    
    while n >= 0:
        empty_list.append(lst[n])
        n = n - 1
    
    return empty_list

print(reverse_list([1, 2, 3, 4, 5]))