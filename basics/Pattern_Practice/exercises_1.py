"""
Problem: Square of side 'N'

Description:
    You are given an integer n. Your task is to return a square pattern of size n x n 
    made up of the character '*', represented as a list of strings.

Input Parameters:
    n (int): The size of the square (number of rows and columns).

Output:
    List[str]: A list of strings where each string is a row of n characters.

Examples:
    Input: 3
    Output: ['***', '***', '***']

    Input: 5
    Output: ['*****', '*****', '*****', '*****', '*****']
"""

def generate_square(n):
    """
    Function to return a square pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The size of the square.
    
    Returns:
    list: A list of strings where each string represents a row of the square.
    """
    empty_list = []
    for i in range(n):
        empty_list.append(n * '*')
        
    return empty_list
    
result = generate_square(3)
print(result)