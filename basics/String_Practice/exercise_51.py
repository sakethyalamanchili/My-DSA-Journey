"""
Problem: Check Subsequence

Description:
    You are given two strings s and t. Your task is to determine if string t is 
    a subsequence of string s. 
    
    *Definition:* A subsequence is formed by deleting some (or no) characters 
    from the original string without changing the relative order of the 
    remaining characters.

Input Parameters:
    s (str): The source string (the longer one).
    t (str): The target string (the potential subsequence).

Output:
    bool: True if t is a subsequence of s, False otherwise.

Examples:
    Input: s = "abcde", t = "ace"
    Output: True
    # 'a', 'c', 'e' appear in s in that order.

    Input: s = "abcde", t = "aec"
    Output: False
    # 'e' appears before 'c' in s, so order is broken.
"""

def is_subsequence(s, t):
    # Your code here
    pass

s = "abcde"
t = "ace"
order = []

for idx, letter in enumerate(s):
    if letter in t:
        order.append(idx)

for i in range(len(order)):
    if order[i] < order[i+1]:
        print(True)
    else:
        print(False)