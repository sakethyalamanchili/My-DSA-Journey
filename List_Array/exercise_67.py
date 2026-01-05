"""
Problem: Reverse a List (In-Place)

Description:
    Given a list of integers, write a function to reverse the order of elements 
    in the list.
    
    *Constraint:* Try to do this "in-place" (modifying the original list) 
    rather than creating a new list, to save memory.
    *Companies:* Google, Amazon, Microsoft, Apple

Input Parameters:
    lst (List[int]): A list of integers.

Output:
    List[int]: The list with elements in reversed order.

Examples:
    Input: lst = [1, 2, 3, 4, 5]
    Output: [5, 4, 3, 2, 1]

    Input: lst = [10, 20, 30]
    Output: [30, 20, 10]
"""

def reverse_list(lst):
    start = 0
    end = len(lst)-1
    while start < end:
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1
    return lst

print(reverse_list(lst = [1, 2, 3, 4, 5]))
print(reverse_list(lst = [10, 20, 30]))