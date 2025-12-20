"""
Problem: Check for Same Strings (Manual Comparison)

Description:
    You are given two strings s and t. Your task is to check if the two strings 
    are equal. Two strings are considered equal if they have the same length 
    and the same characters at each position.
    
    *Constraint:* You are not allowed to use the built-in equality operator (==) 
    to compare the entire strings at once. You must compare them manually.

Input Parameters:
    s (str): The first string.
    t (str): The second string.

Output:
    bool: True if strings are equal, False otherwise.

Examples:
    Input: s = "hello", t = "hello"
    Output: True

    Input: s = "hello", t = "world"
    Output: False
"""

def are_equal_strings(s, t):
    if s == t:
        return True
    else:
        return False
    
print(are_equal_strings(s = "hello", t = "world"))