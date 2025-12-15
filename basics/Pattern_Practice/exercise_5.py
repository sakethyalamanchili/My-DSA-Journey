"""
Problem: Inverted Right Angled Triangle

Description:
    You are given an integer n. Your task is to return an inverted right-angled triangle 
    pattern of '*' where the first row has n stars, the second row n-1 stars, and so on, 
    until the last row has 1 star.

Input Parameters:
    n (int): The height and base of the triangle.

Output:
    List[str]: A list of strings where the i-th row contains decreasing numbers of stars.

Examples:
    Input: 3
    Output: ['***', '**', '*']

    Input: 5
    Output: ['*****', '****', '***', '**', '*']
"""

def generate_inverted_triangle(n):
    empty_list = []
    i = 1
    
    while i <= n:
        empty_list.append(n * '*')
        n = n - 1
    
    return empty_list
        
result = generate_inverted_triangle(5)
print(result)