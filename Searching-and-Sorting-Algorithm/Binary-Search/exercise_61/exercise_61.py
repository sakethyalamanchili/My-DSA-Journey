"""
Problem: Find First and Last Position of Element in Sorted Array

Description:
    Given an array of integers 'nums' sorted in non-decreasing order, and an 
    integer 'target', find the starting and ending position of the given 'target' 
    value. If 'target' is not found in the array, return [-1, -1].

    *Complexity Constraint:* You must write an algorithm with O(log n) runtime complexity.
    *Companies:* Goldman Sachs, Amazon, Wipro, Airtel
    *LeetCode:* https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

Input Parameters:
    nums (List[int]): A list of integers sorted in non-decreasing order.
    target (int): The target value to search for.

Output:
    List[int]: [start_index, end_index] of the target. Returns [-1, -1] if not found.

Examples:
    Input: nums = [5, 7, 7, 8, 8, 10], target = 8 
    Output: [3, 4]

    Input: nums = [5, 7, 7, 8, 8, 10], target = 6 
    Output: [-1, -1]
"""

def searchRange(nums, target):
    
    def first_bound(is_first):
        start = 0
        end = len(nums) - 1
        bound = -1
        
        while start <= end:
            middle = (start + end) // 2
            
            if nums[middle] == target:
                bound = middle
                if is_first:
                    # Left Bias
                    end = middle - 1
                else:
                    # Right Bias
                    start = middle + 1
            
            elif nums[middle] < target:
                start = middle + 1
            
            else:
                end = middle - 1
        return bound
    
    start_index = first_bound(is_first=True)
    
    if start_index == -1: # If Target not found in nums.
        return [-1, -1]
    
    # If Target not found in start step, it def wil not be found in end.
    end_index = first_bound(is_first=False)
    
    return [start_index, end_index]

print(searchRange(nums = [5, 7, 7, 8, 8, 10], target = 8))