"""
Problem: Plus One

Description:
    You are given a large integer represented as an integer array 'digits'.
    The digits are ordered from most significant to least significant.
    Your task is to increment the large integer by one and return the 
    resulting array of digits.

    *Challenge:* You must handle the "carry" operation manually (e.g., 9 + 1 = 10).
    *Companies:* Google, Amazon, Microsoft, Facebook
    *LeetCode:* https://leetcode.com/problems/plus-one/

Input Parameters:
    digits (List[int]): A list of integers representing the digits.

Output:
    List[int]: The list representing the number after incrementing by one.

Examples:
    Input: digits = [1, 2, 3]
    Output: [1, 2, 4]

    Input: digits = [4, 3, 2, 1]
    Output: [4, 3, 2, 2]

    Input: digits = [9, 9, 9]
    Output: [1, 0, 0, 0]
"""

def plus_one(digits):
    """
    Function to increment a large integer represented as a list of digits by one.
    :param digits: List[int] -> List of digits representing the large integer
    :return: List[int] -> The list representing the integer after incrementing
    """
    char = ""
    
    for i in digits:
        char = char + str(i)
        
    str_int = int(char)
    operation = str_int + 1
    int_str = str(operation)
    result = []
    
    for j in int_str:
        result.append(int(j))
        
    return result

print(plus_one(digits = [1, 2, 3]))