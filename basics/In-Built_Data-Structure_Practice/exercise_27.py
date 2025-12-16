"""
Problem: Find Maximum Difference Between Two Consecutive Elements (Brute Force)

Description:
    You are given a list of integers. Write a Python program to find the maximum 
    difference between two consecutive elements in the list using a brute-force approach. 
    The difference is defined as the absolute value of the difference.

Input Parameters:
    lst (List[int]): A list of integers.

Output:
    int: The maximum absolute difference between any two consecutive elements.

Examples:
    Input: lst = [1, 7, 3, 10, 5]
    Output: 7  (|3 - 10| = 7)

    Input: lst = [10, 11, 15, 3]
    Output: 12 (|15 - 3| = 12)
"""

def max_consecutive_difference(lst):
    if len(lst) < 2:
        return 0

    differences = []
    
    for i in range(len(lst) - 1):
        diff = abs(lst[i] - lst[i + 1])
        differences.append(diff)
    
    return max(differences)

lst = [1, 7, 3, 10, 5]
print(max_consecutive_difference(lst))