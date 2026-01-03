"""
Problem: Find Minimum in Rotated Sorted Array

Description:
    Given a sorted array of length n that has been rotated between 1 and n times, 
    find the minimum element in the array. The array was originally sorted in 
    ascending order.

    *Constraint:* You must write an algorithm that runs in O(log n) time.
    *Companies:* Google, Arcesium, PhonePe, Qualcomm
    *LeetCode:* https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

Input Parameters:
    nums (List[int]): A list of unique integers sorted in ascending order 
                      but rotated at an unknown pivot.

Output:
    int: The minimum element in the array.

Examples:
    Input: nums = [4, 5, 6, 7, 0, 1, 2]
    Output: 0
    # Explanation: Original was [0, 1, 2, 4, 5, 6, 7]. Rotated 4 times.

    Input: nums = [11, 13, 15, 17]
    Output: 11
    # Explanation: Sorted but not rotated (or rotated 0 times).
"""

def findMin(nums):
    start = 0
    end = len(nums)-1
    while start < end:
        middle = (start + end) // 2
        if nums[middle] > nums[end]:
            start = middle + 1
        else:
            end = middle
    return nums[start]

print(findMin(nums = [3, 1, 2]))