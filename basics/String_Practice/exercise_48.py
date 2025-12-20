"""
Problem: Remove Duplicates in a String (Preserving Order)

Description:
    You are given a string s. Your task is to remove duplicate characters from 
    the string while preserving the order of the first occurrences and return 
    the modified string.

Input Parameters:
    s (str): The input string to clean.

Output:
    str: A string containing only the unique characters from s, in their original order.

Examples:
    Input: "programming"
    Output: "progamin"

    Input: "Hello, World!"
    Output: "Helo, Wrd!"
"""

def remove_duplicates(s):
    empty_string = ""
    for letter in s:
        if letter not in empty_string:
            empty_string += letter
    
    return empty_string

print(remove_duplicates("programming"))