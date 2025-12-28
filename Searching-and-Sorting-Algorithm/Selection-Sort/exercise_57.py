"""
Problem: Selection Sort Algorithm

Description:
    You are given a list of integers. Write a Python function to sort the list 
    in ascending order using the Selection Sort algorithm. 
    
    *Logic:* Selection Sort works by repeatedly finding the minimum element 
    from the unsorted part of the list and swapping it with the first element 
    of the unsorted part.

Input Parameters:
    lst (List[int]): The list to be sorted.

Output:
    List[int]: The list sorted in ascending order.

Examples:
    Input: lst = [64, 25, 12, 22, 11]
    Output: [11, 12, 22, 25, 64]

    Input: lst = [29, 10, 14, 37, 13]
    Output: [10, 13, 14, 29, 37]
"""

def selection_sort(lst):
    n = len(lst)
    for i in range(0, n-1):
        minIndex = i
        for j in range(i+1, n):
            if lst[j] < lst[minIndex]:
                minIndex = j
        if i != minIndex:
            lst[i], lst[minIndex] = lst[minIndex], lst[i]
    return lst

print(selection_sort(lst = [64, 25, 12, 22, 11]))