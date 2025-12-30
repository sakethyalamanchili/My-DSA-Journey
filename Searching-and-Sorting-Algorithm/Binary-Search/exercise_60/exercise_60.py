"""
Problem: Find Smallest Letter Greater Than Target

Description:
    You are given a sorted array of characters 'letters' (non-decreasing order) 
    and a character 'target'. Your task is to return the smallest character in 
    'letters' that is lexicographically greater than 'target'.

    *Constraint:* If such a character does not exist (i.e., target is greater 
    than or equal to everything in the list), return the first character in 'letters'.
    
    *Companies:* JP Morgan, TCS, Wells Fargo, Gameskraft
    *LeetCode:* https://leetcode.com/problems/find-smallest-letter-greater-than-target/

Input Parameters:
    letters (List[str]): A sorted list of characters.
    target (str): The character to compare against.

Output:
    str: The smallest character strictly greater than target, or the first 
         character if none exists.

Examples:
    Input: letters = ['c', 'f', 'j'], target = 'a'
    Output: 'c' (Smallest char > 'a' is 'c')

    Input: letters = ['c', 'f', 'j'], target = 'c'
    Output: 'f' (Smallest char > 'c' is 'f')

    Input: letters = ['c', 'f', 'j'], target = 'k'
    Output: 'c' (No char > 'k', so wrap around to start)
"""

def next_greatest_letter(letters, target):
    start = 0
    end = len(letters) - 1
    result = letters[0]
    while start <= end:
        mid = (start + end) // 2
        if target < letters[mid]:
            end = mid - 1
            result = letters[mid]
        else:
            start = mid + 1
    return result

print(next_greatest_letter(letters = ['c', 'f', 'j'], target = 'k'))