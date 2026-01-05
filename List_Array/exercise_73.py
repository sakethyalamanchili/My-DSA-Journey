"""
Problem: Intersection of Two Arrays

Description:
    Given two integer arrays 'nums1' and 'nums2', return an array of their 
    intersection. 
    
    *Constraint:* Each element in the result must be unique, and you may return 
    the result in any order.
    *Companies:* Google, Amazon, Microsoft, Facebook
    *LeetCode:* https://leetcode.com/problems/intersection-of-two-arrays/

Input Parameters:
    nums1 (List[int]): The first array of integers.
    nums2 (List[int]): The second array of integers.

Output:
    List[int]: An array of unique integers present in both arrays.

Examples:
    Input: nums1 = [1, 2, 2, 1], nums2 = [2, 2]
    Output: [2]
    # Explanation: The only number present in BOTH lists is 2. 
    # Even though 2 appears multiple times, the result must be unique.

    Input: nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4]
    Output: [9, 4] (or [4, 9])
"""

def intersection(nums1, nums2):
    """
    Function to find the intersection of two integer arrays.
    :param nums1: List[int] -> First array of integers
    :param nums2: List[int] -> Second array of integers
    :return: List[int] -> An array of unique integers present in both arrays
    """
    result = []
    
    if len(nums1) >= len(nums2):
        max = nums1
        min = nums2
    else:
        max = nums2
        min = nums1
    
    for i in max:
        for j in min:
            if (i == j) and (j not in result):
                result.append(j)
        
    return result

print(intersection(nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4]))