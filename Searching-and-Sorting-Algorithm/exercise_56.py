"""
Problem: Bubble Sort Algorithm

Description:
    You are given a list of integers. Write a Python function to sort the list 
    in ascending order using the Bubble Sort algorithm. 
    
    *Logic:* Bubble Sort repeatedly steps through the list, compares adjacent 
    elements, and swaps them if they are in the wrong order. The process is 
    repeated until the list is sorted.

Input Parameters:
    lst (List[int]): The list to be sorted.

Output:
    List[int]: The list sorted in ascending order.

Examples:
    Input: lst = [64, 34, 25, 12, 22, 11, 90]
    Output: [11, 12, 22, 25, 34, 64, 90]

    Input: lst = [5, 1, 4, 2, 8]
    Output: [1, 2, 4, 5, 8]
"""

def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                # SWAP
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swapped = True
        if not swapped:
            break
    return lst

print(bubble_sort(lst = [64, 34, 25, 12, 22, 11, 90]))