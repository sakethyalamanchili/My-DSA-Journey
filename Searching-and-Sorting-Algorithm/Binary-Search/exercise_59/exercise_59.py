"""
Problem: Count Negative Numbers in a Sorted Matrix

Description:
    You are given an m x n matrix grid where each row and column is sorted in 
    non-increasing order (descending). Your task is to return the number of 
    negative numbers present in the matrix.

    *Companies:* Samsung, Oyo, Groww, Dell
    *LeetCode:* https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

Input Parameters:
    grid (List[List[int]]): A 2D matrix where rows and columns are sorted 
                            in non-increasing order.

Output:
    int: The count of negative numbers in the matrix.

Examples:
    Input: grid = [
        [4, 3, 2, 1], 
        [3, 2, 1, -1], 
        [1, 1, -1, -2], 
        [-1, -1, -2, -3]
    ]
    Output: 7
    # Explanation: The negatives are -1, -1, -2, -1, -1, -2, -3.

    Input: grid = [[3, 2], [1, 0]] 
    Output: 0
"""

def countNegatives(grid):
    count = 0
    col = len(grid[0])
    for row in grid:
        start = 0
        end = col - 1
        while start <= end:
            first_neg_index = col
            mid = (start + end) // 2
            if row[mid] < 0:
                first_neg_index = mid
                end = mid - 1
            else:
                start = mid + 1
        count = count + (col - first_neg_index)
    return count

grid = [
    [4, 3, 2, 1], 
    [3, 2, 1, -1], 
    [1, 1, -1, -2], 
    [-1, -1, -2, -3]  
]
print(f"Count: {countNegatives(grid)}")