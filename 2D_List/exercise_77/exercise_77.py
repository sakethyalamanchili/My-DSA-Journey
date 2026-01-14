"""
Problem: Rotate Image (Rotate Matrix 90° Clockwise)

Description:
    You are given an n x n 2D matrix representing an image. Rotate the image 
    by 90 degrees clockwise.
    
    *Constraint:* The rotation must be done IN-PLACE. You cannot allocate 
    another 2D matrix to store the result. You must modify the input matrix directly.
    *Companies:* Zoho, Amazon, Schlumberger, Facebook
    *LeetCode:* https://leetcode.com/problems/rotate-image/

Input Parameters:
    matrix (List[List[int]]): An n x n 2D list of integers.

Output:
    None: Modify the matrix in-place.

Examples:
    Input: matrix = [
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]
    ]
    Output: [
      [7, 4, 1],
      [8, 5, 2],
      [9, 6, 3]
    ]
"""

def rotate(matrix):
    n = len(matrix)
    
    for i in range(n):
        # Transpose
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
    # Reverse
    for i in range(n):
        matrix[i].reverse()
    
    return matrix

print(rotate(matrix = [
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]
    ]))