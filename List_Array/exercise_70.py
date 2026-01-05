"""
Problem: Missing Number

Description:
    Given an array 'nums' containing n distinct numbers in the range [0, n], 
    return the only number in the range that is missing from the array.

    *Key Constraint:* The array contains n numbers, but the range is 0 to n. 
    This means there are (n + 1) slots, so exactly one number is missing.
    *Companies:* Google, Microsoft, Amazon, Facebook
    *LeetCode:* https://leetcode.com/problems/missing-number/

Input Parameters:
    nums (List[int]): A list of distinct integers in the range [0, n].

Output:
    int: The missing number.

Examples:
    Input: nums = [3, 0, 1]
    Output: 2
    # Explanation: n=3. Range is [0, 1, 2, 3]. Missing 2.

    Input: nums = [0, 1]
    Output: 2
    # Explanation: n=2. Range is [0, 1, 2]. Missing 2.
"""

def find_missing_number(nums):
    n = len(nums)
    for i in range(n+1):
        if i not in nums:
            return i
        
print(find_missing_number(nums = [0, 1]))
print(find_missing_number(nums = [3, 0, 1]))