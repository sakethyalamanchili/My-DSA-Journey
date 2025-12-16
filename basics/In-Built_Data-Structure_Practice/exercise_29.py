"""
Problem: Rotate a List (Without Slicing)

Description:
    You are given a list of integers and an integer k. Write a Python function to 
    rotate the list to the right by k positions without using slicing. 
    A rotation shifts elements from the end of the list to the front.

Input Parameters:
    lst (List[int]): The list to be rotated.
    k (int): The number of positions to rotate the list.

Output:
    List[int]: A list of integers rotated by k positions.

Examples:
    Input: lst = [1, 2, 3, 4, 5], k = 2
    Output: [4, 5, 1, 2, 3]

    Input: lst = [10, 20, 30, 40, 50], k = 3
    Output: [30, 40, 50, 10, 20]
"""

def rotate_list(lst, k):
    if not lst: return []
    
    for _ in range(k):
        last_item = lst.pop()
        lst.insert(0, last_item)
        
    return lst

print(rotate_list(lst = [10, 20, 30, 40, 50], k = 3))