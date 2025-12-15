"""
Problem: Number of Rounds of Lift

Description:
    You are given n, the total number of people, and capacity, the maximum number 
    of people the lift can carry. Calculate the number of rounds required to 
    transport all people to the top floor.

Input Parameters:
    n (int): Total number of people.
    capacity (int): Maximum people per lift round.

Output:
    int: The total number of rounds required.

Examples:
    Input: n = 10, capacity = 3
    Output: 4  (3 rounds take 9 people, 1 round takes the last person)

    Input: n = 7, capacity = 4
    Output: 2
"""

def calculate_lift_rounds(n, capacity):
    rounds = n // capacity  
    if n % capacity > 0:    
        rounds += 1
    return rounds

print(calculate_lift_rounds(7, 4))