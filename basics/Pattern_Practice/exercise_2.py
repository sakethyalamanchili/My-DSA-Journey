"""
Problem: Hollow Square of side 'N'

Description:
    You are given an integer n. Your task is to return a hollow square pattern of size n x n 
    made up of the character '*', represented as a list of strings. The hollow square has '*' 
    on the border, and spaces ' ' in the middle (except for side lengths of 1 and 2).

Input Parameters:
    n (int): The size of the square (number of rows and columns).

Output:
    List[str]: A list of strings where each string is a row of n characters, 
    representing a hollow square.

Examples:
    Input: 3
    Output: ['***', '* *', '***']

    Input: 5
    Output: ['*****', '* *', '* *', '* *', '*****']

Note:
    This exercise is primarily for basic code validation.
"""

def generate_hollow_square(n):
    empty_string = []
    for i in range(n):
        if i ==0 or i == (n-1):
            empty_string.append(n * '*')
        else:
            empty_string.append('*' + ' ' * (n-2) + '*')
    
    return empty_string

result = generate_hollow_square(5)
print(result)