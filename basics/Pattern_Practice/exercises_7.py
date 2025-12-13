"""
Problem: Inverted Pyramid Pattern

Description:
    You are given an integer n. Your task is to return an inverted pyramid pattern of '*', 
    where each side has n rows. The first row has (2n - 1) stars, decreasing by 2 stars 
    per row, centered using spaces.

Input Parameters:
    n (int): The number of rows in the inverted pyramid.

Output:
    List[str]: A list of strings where each string represents a row of the inverted pyramid.

Examples:
    Input: 3
    Output: ['*****', ' *** ', '  * ']

    Input: 5
    Output: ['*********', ' ******* ', '  ***** ', '   *** ', '    * ']
"""

def generate_inverted_pyramid(n):
    i = 0
    empty_list = []
    while (n > 0):
        empty_list.append((i * " ") + (((2 * n) - 1) * "*") + (i * " "))
        i = i + 1
        n = n - 1
    return empty_list

result = generate_inverted_pyramid(5)
print(result)