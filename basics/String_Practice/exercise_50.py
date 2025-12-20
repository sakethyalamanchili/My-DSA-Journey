"""
Problem: Check for Anagrams

Description:
    You are given two strings s and t. Your task is to determine if string t is 
    an anagram of string s. 
    
    *Definition:* An anagram is a word or phrase formed by rearranging the 
    characters of a different word or phrase, using all the original characters 
    exactly once.

Input Parameters:
    s (str): The first string.
    t (str): The second string.

Output:
    bool: True if t is an anagram of s, False otherwise.

Examples:
    Input: s = "anagram", t = "nagaram"
    Output: True

    Input: s = "rat", t = "car"
    Output: False
"""

def is_anagram(s, t):
    return sorted(s) == sorted(t)

print(is_anagram(s = "anagram", t = "nagaram"))