"""
Problem: Move Zeroes

Description:
    Given an integer array 'nums', write a function to move all 0s to the end 
    of the array while maintaining the relative order of the non-zero elements.
    
    *Constraint:* You must do this in-place without making a copy of the array.
    *Companies:* Google, Amazon, Microsoft, Facebook
    *LeetCode:* https://leetcode.com/problems/move-zeroes/

Input Parameters:
    nums (List[int]): A list of integers.

Output:
    None: The function should modify the list in-place (return nothing).

Examples:
    Input: nums = [0, 1, 0, 3, 12]
    Output: (Modified nums) [1, 3, 12, 0, 0]

    Input: nums = [0, 0, 1]
    Output: (Modified nums) [1, 0, 0]
"""

def move_zeroes(nums):
    n = len(nums)
    for i in range(n):
        if nums[i] == 0:
            nums.append(nums[i])
            nums.remove(nums[i])
    return nums

print(move_zeroes(nums = [0, 1, 0, 3, 12]))
print(move_zeroes(nums = [0, 0, 1]))