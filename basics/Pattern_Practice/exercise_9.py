"""
Problem: Floyd's Triangle

Description:
    You are given an integer n. Your task is to return the first n rows of Floyd's Triangle, 
    represented as a list of strings. Floyd's Triangle is a triangular array of natural 
    numbers where the first row contains 1, the second row contains 2 and 3, and so on.

Input Parameters:
    n (int): The number of rows in the triangle.

Output:
    List[str]: A list of strings where each string represents a row in Floyd's Triangle.
    The numbers in each row are space-separated.

Examples:
    Input: 5
    Output: ['1', '2 3', '4 5 6', '7 8 9 10', '11 12 13 14 15']

    Input: 3
    Output: ['1', '2 3', '4 5 6']
"""

def generate_floyds_triangle(n):
    num = 1
    empty_list = []
    
    for i in range(1, n+1):
        row = []
        for j in range(i):
            row.append(str(num))
            num = num + 1
        empty_list.append(" ".join(row))
        
    return empty_list


result = generate_floyds_triangle(5)
print(result)