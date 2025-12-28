"""
Problem: Insertion Sort Algorithm

Description:
    You are given a list of integers. Write a Python function to sort the list 
    in ascending order using the Insertion Sort algorithm. 
    
    *Logic:* Insertion Sort builds a sorted section of the list, one element at 
    a time. It picks the next element (key) and shifts older, larger elements 
    to the right to make space for the key in its correct sorted position.

Input Parameters:
    lst (List[int]): The list to be sorted.

Output:
    List[int]: The list sorted in ascending order.

Examples:
    Input: lst = [12, 11, 13, 5, 6]
    Output: [5, 6, 11, 12, 13]

    Input: lst = [31, 41, 59, 26, 41, 58]
    Output: [26, 31, 41, 41, 58, 59]
"""

def insertion_sort(lst):
    n = len(lst)
    for i in range(1, n):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j+1] = lst[j]
            j = j - 1
        lst[j+1] = key
    return lst

print(insertion_sort(lst = [12, 11, 13, 5, 6]))