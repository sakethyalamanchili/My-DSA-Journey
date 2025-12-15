"""
Problem: Right Angled Triangle II

Description:
    You are given an integer n. Your task is to return a right-angled triangle pattern of '*', 
    where each row contains stars aligned to the right. The first row has one star, 
    the second row has two stars, and so on, until the nth row has n stars.

Input Parameters:
    n (int): The height and base of the triangle.

Output:
    List[str]: A list of strings where each string represents a row in the triangle, 
    right-aligned with leading spaces.

Examples:
    Input: 4
    Output: ['   *', '  **', ' ***', '****']

    Input: 3
    Output: ['  *', ' **', '***']
"""

def generate_right_angled_triangle(n):
    empty_list = []
    
    for i in range(n):
        empty_list.append(((n - i - 1) * " ") + ((i + 1) * '*'))
    
    return empty_list

result = generate_right_angled_triangle(4)
print(result)