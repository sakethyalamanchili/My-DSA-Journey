"""
Problem: Pyramid Pattern

Description:
    You are given an integer n. Your task is to return a pyramid pattern of '*' 
    where each side has n rows. The pyramid is centered, starting with 1 star 
    at the top and increasing by 2 stars per row.

Input Parameters:
    n (int): The height of the pyramid.

Output:
    List[str]: A list of strings where each row has centered stars.
    The i-th row (0-indexed) has (n - i - 1) spaces followed by (2*i + 1) stars 
    followed by (n - i - 1) spaces.

Examples:
    Input: 3
    Output: ['  * ', ' *** ', '*****']

    Input: 5
    Output: ['    * ', '   *** ', '  ***** ', ' ******* ', '*********']
"""

def generate_pyramid(n):
    empty_list = []
    
    for i in range(n):
        empty_list.append((n - i - 1) * " " + (2 * i + 1) * '*' + (n - i - 1) * " ")
    
    return empty_list

result = generate_pyramid(5)
print(result)