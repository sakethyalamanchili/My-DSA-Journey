"""
Problem: Search a 2D Matrix (Virtual 1D Array)

Description:
    You are given an m x n integer matrix with two properties:
    1. Each row is sorted in non-decreasing order.
    2. The first integer of each row is greater than the last integer of the previous row.
    
    *Goal:* Write a function that returns True if target is in matrix, False otherwise.
    *Constraint:* You must write an algorithm with O(log(m * n)) time complexity.
    
    *Companies:* Salesforce, Flipkart, Amazon
    *LeetCode:* https://leetcode.com/problems/search-a-2d-matrix/

Input Parameters:
    matrix (List[List[int]]): An m x n matrix (sorted row-major).
    target (int): The value to search for.

Output:
    bool: True if found, False otherwise.

Examples:
    Input: matrix = [
        [1,  3,  5,  7], 
        [10, 11, 16, 20], 
        [23, 30, 34, 60]
    ], target = 3
    Output: True

    Input: matrix = [...same...], target = 13
    Output: False
"""

def search_matrix(matrix, target):
    if not matrix:
        return False
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    start = 0
    end = (rows * cols) - 1

    while start <= end:
        mid_index = (start + end) // 2
        
        # CONVERT 1D index -> 2D coordinates
        mid_element = matrix[mid_index // cols][mid_index % cols]
        
        if mid_element == target:
            return True
        elif mid_element < target:
            start = mid_index + 1
        else:
            end = mid_index - 1
            
    return False

# Test it
matrix = [
    [1,  3,  5,  7], 
    [10, 11, 16, 20], 
    [23, 30, 34, 60]
]
target = 3

print(search_matrix(matrix, target)) # Output: True