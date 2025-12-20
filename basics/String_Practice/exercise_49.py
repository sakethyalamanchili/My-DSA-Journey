"""
Problem: Count Consonants in a String

Description:
    You are given a string s. Your task is to count the number of consonants in 
    the string and return the total count. 
    
    *Definition:* A consonant is any alphabetic character that is not a vowel 
    (a, e, i, o, u).

Input Parameters:
    s (str): The input string to analyze.

Output:
    int: The total count of consonants found.

Examples:
    Input: "Hello, World!"
    Output: 7  ('H', 'l', 'l', 'W', 'r', 'l', 'd')

    Input: "Python Programming"
    Output: 13
"""

def count_consonants(s):
    text = s.lower()
    vowels = "aeiou"
    unclean_text = " .,/?':;!"
    count = 0
    for letter in text:
        
        if (letter not in unclean_text) and (letter not in vowels):
            count += 1
            
    return count

print(count_consonants("Python Programming"))