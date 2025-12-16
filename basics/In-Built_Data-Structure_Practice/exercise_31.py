"""
Problem: Merge Three Dictionaries

Description:
    Design a Python function named merge_three_dictionaries to merge exactly 
    three dictionaries into one. 

Input Parameters:
    dict1 (dict): The first dictionary.
    dict2 (dict): The second dictionary.
    dict3 (dict): The third dictionary.

Output:
    dict: A single dictionary containing all key-value pairs from the three inputs.

Examples:
    Input: ({'a': 1}, {'c': 3}, {'e': 5})
    Output: {'a': 1, 'c': 3, 'e': 5}

    Input: ({'x': 10}, {'z': 30}, {'a': 40})
    Output: {'x': 10, 'z': 30, 'a': 40}
"""

def merge_three_dictionaries(dict1, dict2, dict3):
    dict1.update(dict2) # Add dict2 into dict1
    dict1.update(dict3) # Add dict3 into dict1
    return dict1

print(merge_three_dictionaries({'a': 1}, {'c': 3}, {'e': 5}))