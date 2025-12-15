"""
Problem: Hollow Right Triangle

Description:
    You are given an integer n. Your task is to return a hollow right-angled triangle 
    pattern of '*', where the first and last rows contain stars, while the inner rows 
    contain a star at the beginning and end, with spaces in between. 

Input Parameters:
    n (int): The height of the triangle.

Output:
    List[str]: A list of strings where each string represents a row in the triangle.

Examples:
    Input: 4
    Output: ['*', '**', '* *', '****']

    Input: 5
    Output: ['*', '**', '* *', '* *', '*****']
"""

def generate_hollow_right_angled_triangle(n):  
    result = []
    
    for i in range(1, n + 1):
        if i == 1:
            result.append('*')
        elif i == n:
            result.append(i * '*')
        else:
            spaces = (i - 2) * " "
            result.append("*" + spaces + "*")
            
    return result

print(generate_hollow_right_angled_triangle(5))