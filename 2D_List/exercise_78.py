"""
Problem: Determine Whether Matrix Can Be Obtained By Rotation

Description:
    You are given two n x n binary matrices 'mat' and 'target'. Your task is to 
    determine whether it is possible to make 'mat' equal to 'target' by rotating 
    'mat' in 90-degree increments (clockwise).
    
    *Logic:* You need to check if 'mat' equals 'target' in any of its 4 possible 
    orientations: 0°, 90°, 180°, or 270°.
    
    *Companies:* Oracle, Apple, Wipro
    *LeetCode:* https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

Input Parameters:
    mat (List[List[int]]): The starting n x n binary matrix.
    target (List[List[int]]): The target n x n binary matrix.

Output:
    bool: True if they can match, False otherwise.

Examples:
    Input: mat = [[0, 1], [1, 0]], target = [[1, 0], [0, 1]]
    Output: True
    # Explanation: Rotating mat 90 degrees clockwise makes it equal to target.

    Input: mat = [[0, 1], [1, 1]], target = [[1, 0], [0, 1]]
    Output: False
"""

def can_be_rotated(mat, target):
    n = len(mat)
    
    for i in range(4):
        for j in range(n):
            for k in range(j, n):
                mat[j][k], mat[k][j] = mat[k][j], mat[j][k]
                
        for l in range(n):
            mat[l].reverse()
        
        if mat == target:
            return True
    
    return False

print(can_be_rotated(mat = [[0, 1], [1, 1]], target = [[1, 0], [0, 1]]))