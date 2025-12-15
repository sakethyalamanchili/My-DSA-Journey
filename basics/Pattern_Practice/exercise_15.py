"""
Problem: Number Pyramid Pattern

Description:
    You are given an integer n. Your task is to return a pyramid pattern of numbers, 
    where each row contains increasing numbers starting from 1 up to the row number, 
    and the pyramid is centered with leading spaces.

Input Parameters:
    n (int): The height of the pyramid.

Output:
    List[str]: A list of strings where each string represents a row in the pyramid pattern.

Examples:
    Input: 4
    Output: ['   1   ', '  1 2  ', ' 1 2 3 ', '1 2 3 4']

    Input: 3
    Output: ['  1  ', ' 1 2 ', '1 2 3']
"""

def generate_number_pyramid(n):
    result = []

    for i in range(n):
        row_numbers = []
        for j in range(i + 1):
            row_numbers.append(str(j + 1))

        row_content = " ".join(row_numbers)

        num_spaces = n - 1 - i

        final_row = (num_spaces * ' ') + row_content + (num_spaces * ' ')
        result.append(final_row)

    return result

pyramid = generate_number_pyramid(5)
print(pyramid)