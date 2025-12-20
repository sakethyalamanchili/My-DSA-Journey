"""
Problem: Count Vowels in a String

Description:
    You are given a string s. Your task is to count the number of vowels 
    (both uppercase and lowercase) in the string and return the total count.
    
    *Note:* Vowels are 'a', 'e', 'i', 'o', 'u'.

Input Parameters:
    s (str): The input string to analyze.

Output:
    int: The total count of vowels found.

Examples:
    Input: "Hello, World!"
    Output: 3  ('e', 'o', 'o')

    Input: "Python Programming"
    Output: 4  ('o', 'o', 'a', 'i')
"""

def count_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    c = 0
    
    for i in s:
        if i in vowels:
            c += 1
    
    return c

print(count_vowels("Python Programming"))