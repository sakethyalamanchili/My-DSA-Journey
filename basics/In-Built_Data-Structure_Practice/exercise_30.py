"""
Problem: Merge Lists to Dictionary

Description:
    Design a Python function named merge_lists_to_dictionary to merge two lists 
    into a dictionary where elements from the first list act as keys and 
    elements from the second list act as values.

Input Parameters:
    keys (List): A list of keys.
    values (List): A list of values.

Output:
    dict: A dictionary containing merged key-value pairs.

Examples:
    Input: keys = ['a', 'b', 'c'], values = [1, 2, 3]
    Output: {'a': 1, 'b': 2, 'c': 3}

    Input: keys = ['x', 'y', 'z'], values = [10, 20, 30]
    Output: {'x': 10, 'y': 20, 'z': 30}
"""

def merge_lists_to_dictionary(keys, values):
    result = {}
    
    if len(keys) != len(values):
        return False
    
    for i in range(len(keys)):
        result[keys[i]] = values[i]
    
    return result 

print(merge_lists_to_dictionary(keys = ['a', 'b', 'c'], values = [1, 2, 3]))