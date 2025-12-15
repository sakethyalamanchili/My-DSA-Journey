"""
Problem: Hollow Inverted Right Triangle

Description:
    You are given an integer n. Your task is to return a hollow inverted right-angled 
    triangle pattern of '*', where the first row contains n stars, while the inner rows 
    contain a star at the beginning and end, with spaces in between. 
    The triangle should be left-aligned.

Input Parameters:
    n (int): The height of the triangle.

Output:
    List[str]: A list of strings where each string represents a row in the triangle.

Examples:
    Input: 4
    Output: ['****', '* *', '**', '*']

    Input: 5
    Output: ['*****', '* *', '* *', '**', '*']
"""

def generate_hollow_inverted_right_angled_triangle(n):
    i = 0
    result = []
    while i < n:
        if i == 0:
            result.append(n * '*')
        elif i == (n - 1):
            result.append('*')
        else:
            spaces = (n - i) - 2
            star = "*"
            result.append(star + spaces * " " + star)
        i = i + 1
    return result

print(generate_hollow_inverted_right_angled_triangle(5))