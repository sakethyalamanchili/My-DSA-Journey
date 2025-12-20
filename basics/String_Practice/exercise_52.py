"""
Problem: Check for Substring (Manual Implementation)

Description:
    You are given two strings, s and t. Your task is to determine if the string t 
    is a substring of the string s. 
    
    *Definition:* A substring is a contiguous sequence of characters within a string.
    *Constraint:* Do not use any built-in functions (like 't in s' or 's.find(t)') 
    and do not use recursion.

Input Parameters:
    s (str): The main string to search within.
    t (str): The substring to search for.

Output:
    bool: True if t is found inside s, False otherwise.

Examples:
    Input: s = "hello world", t = "world"
    Output: True

    Input: s = "hello world", t = "worlds"
    Output: False
"""

def is_substring(s, t):
    if not t: 
        return True
        
    n = len(s)
    m = len(t)

    for i in range(n - m + 1):

        current_window = s[i : i + m]

        if current_window == t:
            return True
            
    return False

print(is_substring(s="hello world", t="world")) 
print(is_substring(s="hello world", t="orls")) 