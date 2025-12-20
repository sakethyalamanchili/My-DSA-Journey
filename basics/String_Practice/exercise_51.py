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
    if not t:
        return True
        
    i = 0 
    j = 0 

    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            j += 1
        i += 1

    return j == len(t)

print(is_subsequence("abcde", "aec"))
print(is_subsequence("abcde", "ace"))
print(is_subsequence("abcde", ""))  