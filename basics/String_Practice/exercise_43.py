"""
Problem: Reverse a String

Description:
    You are given a string s. Your task is to return the reversed version of the string.

Input Parameters:
    s (str): The input string to reverse.

Output:
    str: The reversed string.

Examples:
    Input: "hello"
    Output: "olleh"

    Input: "Python"
    Output: "nohtyP"
"""

def reverse_string(s):
    # [start : stop : step]
    # leaving start/stop empty means "the whole thing"
    # -1 step means "walk backwards"
    return s[::-1]

print(reverse_string("Python")) 