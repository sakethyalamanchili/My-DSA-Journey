"""
Problem: Rotate List Left

Description:
    Given a list of integers and an integer D, write a function to rotate 
    the list to the left by D positions.
    
    *Concept:* "Rotating left" means taking the first D elements and moving 
    them to the very end of the list, shifting everything else forward.
    *Companies:* Google, Amazon, Microsoft, Facebook

Input Parameters:
    ARR (List[int]): A list of integers.
    D (int): The number of positions to rotate the list to the left.

Output:
    List[int]: The list after rotating it to the left by D positions.

Examples:
    Input: ARR = [1, 2, 3, 4, 5], D = 2
    Output: [3, 4, 5, 1, 2]
    # Explanation: Elements [1, 2] are moved to the back.

    Input: ARR = [10, 20, 30, 40, 50], D = 3
    Output: [40, 50, 10, 20, 30]
"""

def rotate_left(ARR, D):
    n = len(ARR)
    right = ARR[D:n]
    left = ARR[0:D]
    result = right + left
    return result

print(rotate_left(ARR = [1, 2, 3, 4, 5], D = 2))
print(rotate_left(ARR = [10, 20, 30, 40, 50], D = 3))