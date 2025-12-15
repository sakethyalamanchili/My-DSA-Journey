"""
Problem: Sandglass Pattern

Description:
    You are given an integer n. Your task is to return a sandglass pattern of '*', 
    where the first row contains 2n - 1 stars and decreases to 1 star, 
    then increases back to 2n - 1 stars.

Input Parameters:
    n (int): The size of the half-glass (height of the top inverted pyramid).

Output:
    List[str]: A list of strings where each string represents a row in the sandglass.

Examples:
    Input: 3
    Output: ['*****', ' *** ', '  * ', ' *** ', '*****']

    Input: 4
    Output: ['*******', ' ***** ', '  *** ', '   * ', '  *** ', ' ***** ', '*******']
"""

def generate_sandglass(n):
    result = []
    
    for i in range(n):
        stars = (2 * (n - i) - 1) * '*'
        spaces = i * ' '
        result.append(spaces + stars + spaces)

    for i in range(1, n):
        stars = (2 * i + 1) * '*'
        spaces = (n - i - 1) * ' '
        result.append(spaces + stars + spaces)
        
    return result

print(generate_sandglass(3))