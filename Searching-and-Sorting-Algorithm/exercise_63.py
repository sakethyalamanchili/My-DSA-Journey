"""
Problem: Search in Rotated Sorted Array

Description:
    Given a sorted array that has been rotated at an unknown pivot, find the 
    index of a given target value. 
    
    *Constraint:* You must write an algorithm with O(log n) runtime complexity.
    *Companies:* Microsoft, Amazon, Uber
    *LeetCode:* https://leetcode.com/problems/search-in-rotated-sorted-array/

Input Parameters:
    nums (List[int]): A list of integers sorted in ascending order but 
                      rotated at an unknown pivot.
    target (int): The integer value to search for.

Output:
    int: The index of the target value, or -1 if not found.

Examples:
    Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 0
    Output: 4

    Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 3
    Output: -1
"""

def search(nums, target):
    start = 0
    end = len(nums)-1
    
    while start <= end:
        mid = (start + end) // 2
        
        if target == nums[mid]:
            return mid
        
        if nums[mid] <= nums[end]:
            if nums[mid] < target <= nums[end]:
                start = mid + 1
            else:
                end = mid - 1
        else:
            if nums[start] <= target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        
    return -1
    
print(search(nums = [4, 5, 6, 7, 0, 1, 2], target = 0)) 