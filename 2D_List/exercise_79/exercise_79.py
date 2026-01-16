"""
Problem: Spiral Matrix

Description:
    You are given an m x n matrix. Write a function that returns all the 
    elements of the matrix in spiral order.
    
    *Traversal Order:* 1. Left to Right (Top row)
    2. Top to Bottom (Right column)
    3. Right to Left (Bottom row)
    4. Bottom to Top (Left column)
    ... Repeat until done.

    *Companies:* Apple, Adobe, Paytm, Jio
    *LeetCode:* https://leetcode.com/problems/spiral-matrix/

Input Parameters:
    matrix (List[List[int]]): A 2D list representing the matrix of size m x n.

Output:
    List[int]: A list of integers representing the elements in spiral order.

Examples:
    Input: matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]

    Input: matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    Output: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
"""

def spiral_order(matrix):
    # Edge Case
    if not matrix:
        return []
    
    top = 0
    bottom = len(matrix)-1
    left = 0
    right = len(matrix[0])-1
    
    result = []
    
    while top <= bottom and left <= right:
        for i in range(left, right+1):
            result.append(matrix[top][i])
        top += 1
        
        for j in range(top, bottom+1):
            result.append(matrix[j][right])
        right -= 1
        
        for k in range(right, left-1, -1):
            result.append(matrix[bottom][k])
        bottom -= 1
        
        for l in range(bottom, top-1, -1):
            result.append(matrix[l][left])
        left += 1
        
    return result

print(spiral_order(matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]))