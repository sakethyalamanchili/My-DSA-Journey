"""
Problem: Merge Two Sorted Lists

Description:
    You are given two sorted lists of integers. Write a Python function to merge 
    these two sorted lists into one sorted list. The resulting list should also 
    be in non-decreasing order.

Input Parameters:
    list1 (List[int]): The first sorted list.
    list2 (List[int]): The second sorted list.

Output:
    List[int]: A single merged list containing all elements, sorted.

Examples:
    Input: list1 = [1, 3, 5], list2 = [2, 4, 6]
    Output: [1, 2, 3, 4, 5, 6]

    Input: list1 = [1, 4, 7], list2 = [2, 3, 5, 8]
    Output: [1, 2, 3, 4, 5, 7, 8]
"""

def merge_two_sorted_lists(list1, list2):
    merged = list1 + list2
    return sorted(merged)

print(merge_two_sorted_lists([1, 3, 5], [2, 4, 6]))