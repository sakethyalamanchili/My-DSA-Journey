"""
Problem: Diamond Pattern

Description:
    You are given an integer n. Your task is to return a diamond pattern of '*' 
    with 2n - 1 rows. The upper part (n rows) increases like a pyramid, 
    and the lower part (n-1 rows) decreases like an inverted pyramid.

Input Parameters:
    n (int): The size of the upper half (including the middle row).

Output:
    List[str]: A list of strings where each string represents a row in the diamond.

Examples:
    Input: 3
    Output: ['  * ', ' *** ', '*****', ' *** ', '  * ']

    Input: 5
    Output: ['    * ', '   *** ', '  ***** ', ' ******* ', '*********', 
             ' ******* ', '  ***** ', '   *** ', '    * ']
"""

def generate_diamond(n):
    empty_list = []
    
    for i in range(n):
        empty_list.append(((n - i - 1) * " ") + (((2 * i) + 1) * '*') + ((n - i - 1) * " "))
    n = n - 1
    i = 0
    while n > 0:
        empty_list.append(((i + 1) * " ") + (((2 * n) - 1) * '*') + ((i + 1) * " "))
        n = n - 1
        i = i + 1

    return empty_list

result = generate_diamond(5)
print(result)