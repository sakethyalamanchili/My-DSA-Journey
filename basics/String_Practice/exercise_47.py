"""
Problem: Count Words in a String

Description:
    You are given a string s. Your task is to count the number of words in the string 
    and return the total count. A word is defined as a sequence of characters 
    separated by spaces.

Input Parameters:
    s (str): The input string to analyze.

Output:
    int: The total count of words found.

Examples:
    Input: "Hello, World!"
    Output: 2

    Input: "Python programming is fun."
    Output: 4
"""

def count_words(s):
    split = s.split()
    count = 0
    for word in split:
        count += 1
    return count

print(count_words("Hello, World!"))