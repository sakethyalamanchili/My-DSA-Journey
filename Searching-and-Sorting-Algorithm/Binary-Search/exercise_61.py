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
    start = 0
    end = len(nums) - 1
    result = [-1, -1]
    while start <= end:
        middle = (start + end) // 2
        if nums[middle] < target:
            start = middle + 1
        elif nums[middle] == target:
            if (nums[middle + 1] == target):
                result = [middle, (middle + 1)]
                break
            elif (nums[middle - 1] == target):
                result = [middle - 1, middle]
                break
        else:
            end = middle - 1
    return result

print(searchRange(nums = [5, 7, 7, 8, 8, 10], target = 6))