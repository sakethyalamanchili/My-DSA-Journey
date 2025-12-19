"""
Problem: Sum of N Even Natural Numbers

Description:
    You are given an integer n. Your task is to calculate and return the sum of 
    the first n even natural numbers. The even natural numbers are: 2, 4, 6, 8, ...

Input Parameters:
    n (int): The count of even numbers to sum.

Output:
    int: The sum of the first n even natural numbers.

Examples:
    Input: n = 3
    Output: 12  (2 + 4 + 6)

    Input: n = 5
    Output: 30  (2 + 4 + 6 + 8 + 10)
"""

def sum_of_even_numbers(n):
    sum = 0
    for i in range(1, (2*n+1)):
        if i % 2 == 0:
            sum = sum + i
    
    return sum

print(sum_of_even_numbers(5))