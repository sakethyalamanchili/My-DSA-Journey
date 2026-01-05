"""
Problem: Max Consecutive Ones

Description:
    Given a binary array 'nums', return the maximum number of consecutive 
    1s in the array.
    
    *Constraint:* The input array contains only 0s and 1s.
    *Companies:* Google, Amazon, Microsoft, Facebook
    *LeetCode:* https://leetcode.com/problems/max-consecutive-ones/

Input Parameters:
    nums (List[int]): A binary array (elements are 0 or 1).

Output:
    int: The maximum count of consecutive 1s.

Examples:
    Input: nums = [1, 1, 0, 1, 1, 1]
    Output: 3
    # Explanation: The first two digits are 1s, then a 0, then three 1s. 
    # The maximum consecutive count is 3.

    Input: nums = [1, 0, 1, 1, 0, 1]
    Output: 2
"""

def find_max_consecutive_ones(nums):
    current_streak = 0
    max_streak = 0
    for num in nums:
        if num == 1:
            current_streak += 1
            if current_streak > max_streak:
                max_streak = current_streak
        
        else:
            current_streak = 0
    
    return max_streak

print(find_max_consecutive_ones(nums = [1, 1, 0, 1, 1, 1]))
print(find_max_consecutive_ones(nums = [1, 0, 1, 1, 0, 1]))