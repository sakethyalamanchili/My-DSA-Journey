"""
Problem: Length of the Longest Word (Manual Implementation)

Description:
    You are given a string s. Your task is to find the length of the longest word 
    in the string. A word is defined as a sequence of characters separated by spaces.
    
    *Constraint:* Do not use any built-in functions for string manipulation 
    (like split() or max()).

Input Parameters:
    s (str): The input string to analyze.

Output:
    int: The length of the longest word found.

Examples:
    Input: "The quick brown fox jumps over the lazy dog"
    Output: 5  ("quick", "brown", "jumps" are all 5)

    Input: "Hello World"
    Output: 5
"""

def longest_word_length(s):
    max_length = 0
    current_length = 0
    s = s + " "
    
    for char in s:
        if char != " ":
            current_length += 1
        else:
            if current_length > max_length:
                max_length = current_length
            
            current_length = 0
            
    return max_length

print(longest_word_length("The quick brown fox jumps"))
print(longest_word_length("Hello World"))