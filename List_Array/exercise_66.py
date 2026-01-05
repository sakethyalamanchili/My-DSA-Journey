"""
Problem: Palindrome List

Description:
    Given a list of integers, determine if it is a palindrome. 
    A list is considered a palindrome if it reads the same forward and backward.
    
    *Companies:* Google, Amazon, Microsoft, Facebook

Input Parameters:
    lst (List[int]): A list of integers.

Output:
    bool: True if the list is a palindrome, False otherwise.

Examples:
    Input: lst = [7, 8, 9, 8, 7]
    Output: True

    Input: lst = [1, 2, 3, 4, 5]
    Output: False

    Input: lst = [1, 2, 3, 2, 1]
    Output: True
"""

def is_palindrome(lst):
    start = 0
    end = len(lst)-1
    while start < end:
        if lst[start] != lst[end]:
            return False
        start += 1
        end -= 1
    return True

print(is_palindrome(lst = [7, 8, 9, 8, 7]))
print(is_palindrome(lst = [1, 2, 3, 4, 5]))
print(is_palindrome(lst = [1, 2, 3, 2, 1]))