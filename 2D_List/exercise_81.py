"""
Problem: Reshape the Matrix

Description:
    In MATLAB, there is a handy function called reshape that reshapes a matrix 
    of dimensions m x n into a new one with a different size r x c keeping 
    its original data in row-traversing order.
    
    You are given an m x n matrix 'mat' and two integers 'r' and 'c' representing 
    the number of rows and columns of the wanted reshaped matrix.
    
    *Constraint:* If the reshape operation is not possible (i.e., the total elements 
    m * n does not equal r * c), return the original matrix.
    
    *Companies:* Dunzo, Flipkart
    *LeetCode:* https://leetcode.com/problems/reshape-the-matrix/

Input Parameters:
    mat (List[List[int]]): A 2D list representing an m x n matrix.
    r (int): The target number of rows.
    c (int): The target number of columns.

Output:
    List[List[int]]: The reshaped matrix or the original matrix.

Examples:
    Input: mat = [[1, 2], [3, 4]], r = 1, c = 4
    Output: [[1, 2, 3, 4]]

    Input: mat = [[1, 2], [3, 4]], r = 2, c = 4
    Output: [[1, 2], [3, 4]]
    # Explanation: Original size is 2x2 = 4 elements. Target is 2x4 = 8 elements.
    # Reshape is impossible, return original.
"""

def matrix_reshape(mat, r, c):
    """
    Function to reshape a matrix.
    :param mat: List[List[int]] -> The original matrix
    :param r: int -> Number of rows in reshaped matrix
    :param c: int -> Number of columns in reshaped matrix
    :return: List[List[int]] -> The reshaped matrix or original matrix if not possible
    """
    m, n = len(mat), len(mat[0])
    total_elements = m * n
    
    if total_elements != (r*c):
        return mat
    
    flat = []
    for i in range(m):
        for j in range(n):
            flat.append(mat[i][j])
    
    result = []
    for k in range(r):
        start_idx = k * c
        end_idx = start_idx + c
        result.append(flat[start_idx : end_idx])
    return result            

print(matrix_reshape(mat = [[1, 2], [3, 4]], r = 2, c = 4))