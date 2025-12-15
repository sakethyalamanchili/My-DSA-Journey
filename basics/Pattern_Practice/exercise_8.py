"""
Problem: Right Angled Triangle with Numbers

Description:
    You are given an integer n. Your task is to return a right-angled triangle pattern 
    where each row contains repeated digits. The first row has '1', the second '22', 
    and so on until the nth row has n repeated n times.

Input Parameters:
    n (int): The height of the triangle.

Output:
    List[str]: A list of strings where the i-th row (1-indexed) contains the 
    digit 'i' repeated 'i' times.

Examples:
    Input: 5
    Output: ['1', '22', '333', '4444', '55555']

    Input: 3
    Output: ['1', '22', '333']
"""

def generate_number_triangle(n):
    empty_list = []
    
    for i in range(n):
        empty_list.append((i+1) * str(i+1))
        
    return empty_list

result = generate_number_triangle(5)
print(result)