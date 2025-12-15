"""
Problem: Right Angled Triangle

Description:
    You are given an integer n. Your task is to return a right-angled triangle pattern 
    of '*' where each side has n characters, represented as a list of strings. 
    The triangle starts with 1 star in the first row and increases by 1 each row.

Input Parameters:
    n (int): The height and base of the triangle.

Output:
    List[str]: A list of strings where the i-th row contains i+1 stars.

Examples:
    Input: 3
    Output: ['*', '**', '***']

    Input: 5
    Output: ['*', '**', '***', '****', '*****']
"""

def generate_triangle(n):
    empty_list = []
    
    for i in range(n):
        empty_list.append((i+1) * '*')
        
    return empty_list

result = generate_triangle(5)
print(result)