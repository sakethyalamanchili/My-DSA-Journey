"""
Problem: Rectangle Pattern

Description:
    You are given two integers, n and m. Your task is to return a rectangle pattern of '*', 
    where n represents the number of rows (length) and m represents the number of columns (breadth).

Input Parameters:
    n (int): The number of rows.
    m (int): The number of columns.

Output:
    List[str]: A list of strings where each string represents a row of the rectangle pattern.
 
Examples:
    Input: n = 4, m = 5
    Output: ['*****', '*****', '*****', '*****']

    Input: n = 3, m = 2
    Output: ['**', '**', '**']
"""
    
def generate_rectangle(n, m):
    empty_list = []
    
    for i in range(n):
        empty_list.append(m * '*')
    
    return empty_list

result = generate_rectangle(3, 2)
print(result)