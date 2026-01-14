"""
Problem: Maximum Subarray Sum (Kadane's Algorithm)

Description:
    Given an integer array 'arr', find the sum of the contiguous subarray 
    (containing at least one number, or empty) which has the largest sum.
    
    *Logic:* We iterate through the array while keeping a running sum. 
    If the running sum ever becomes negative, we discard it (reset to 0) 
    because a negative prefix will never help us maximize a future series.
    
    *Companies:* Accenture, SAP Labs, Dunzo, Acko
    *Link:* https://www.naukri.com/code360/problems/maximum-subarray-sum_630526

Input Parameters:
    arr (List[int]): A list of integers (can be positive or negative).

Output:
    int: The maximum subarray sum found.

Examples:
    Input: arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    Output: 6
    # Explanation: The subarray [4, -1, 2, 1] sums to 6.

    Input: arr = [-1, -2, -3]
    Output: 0
    # Explanation: Since an empty subarray is allowed and all numbers are negative,
    # the max sum is 0 (an empty list).
"""

def max_subarray_sum(arr):
    max_sum = 0        # The highest sum found so far
    current_sum = 0    # The sum of the current chain

    for num in arr:
        current_sum += num
        
        # 1. Update max if we found a new high
        if current_sum > max_sum:
            max_sum = current_sum
            
        # 2. Reset if we drop below zero
        if current_sum < 0:
            current_sum = 0
            
    return max_sum

print(max_subarray_sum(arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(max_subarray_sum(arr = [-1, -2, -3]))
