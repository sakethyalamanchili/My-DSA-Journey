"""
Problem: Pascal's Triangle

Description:
    Given an integer 'numRows', return the first numRows of Pascal's triangle.
    In Pascal's triangle, each number is the sum of the two numbers directly 
    above it.
    
    *Structure:*
    - Row 0: [1]
    - Row 1: [1, 1]
    - Row 2: [1, 2, 1]  (1+1=2)
    - Row 3: [1, 3, 3, 1] (1+2=3, 2+1=3)

    *Companies:* Google, Amazon, Microsoft, Facebook
    *LeetCode:* https://leetcode.com/problems/pascals-triangle/

Input Parameters:
    numRows (int): The number of rows to generate.

Output:
    List[List[int]]: A list of lists representing the triangle rows.

Examples:
    Input: numRows = 5
    Output: [
      [1],
      [1, 1],
      [1, 2, 1],
      [1, 3, 3, 1],
      [1, 4, 6, 4, 1]
    ]
"""

def generate(numRows):
    triangle = [[1]] # Initial List
    
    for i in range(1, numRows):
        prev_row = triangle[i-1]
        current_row = [1]
        
        for j in range(1, i):
            sum_row = prev_row[j-1] + prev_row[j]
            current_row.append(sum_row)
        
        current_row.append(1)
        triangle.append(current_row)
        
    return triangle


print(generate(5))