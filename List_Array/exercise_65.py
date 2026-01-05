"""
Problem: Sum of Elements in a List (Manual Implementation)

Description:
    Given a list of integers, write a function to find the sum of all the 
    elements in the list.
    
    *Constraint:* Try to implement this using a loop instead of the built-in 
    sum() function to practice the accumulation pattern.
    *Companies:* Google, Amazon, Microsoft, Facebook

Input Parameters:
    lst (List[int]): A list of integers.

Output:
    int: The sum of all the elements in the list.

Examples:
    Input: lst = [1, 2, 3, 4, 5]
    Output: 15

    Input: lst = [-1, -2, -3, -4]
    Output: -10

    Input: lst = [7]
    Output: 7
"""

def sum_of_elements(lst):
    """
    Function to find the sum of all elements in the list.
    :param lst: List[int] -> List of integers
    :return: int -> The sum of all elements in the list
    """
    sum = 0
    for i in range(len(lst)):
        sum = sum + lst[i]
    return sum

print(sum_of_elements(lst = [7]))