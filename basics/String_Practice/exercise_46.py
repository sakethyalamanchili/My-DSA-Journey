"""
Problem: Check Palindrome (Ignoring Case & Punctuation)

Description:
    You are given a string s. Your task is to check if the string is a palindrome. 
    A string is considered a palindrome if it reads the same forward and backward, 
    ignoring spaces, punctuation, and case.

Input Parameters:
    s (str): The input string to check.

Output:
    bool: True if the string is a palindrome, False otherwise.

Examples:
    Input: "A man a plan a canal Panama"
    Output: True
    # Cleaned: "amanaplanacanalpanama" (reads same both ways)

    Input: "Hello, World!"
    Output: False
    # Cleaned: "helloworld" (reverse is "dlrowolleh")
"""

def is_palindrome(s):
    output = ""
    text = s.lower()
    
    for letter in text:
        if letter not in " ,.:;-_":
            output += letter
    
    if output == output[::-1]:
        return True
    else:
        return False
    
print(is_palindrome("A man a plan a canal Panama"))