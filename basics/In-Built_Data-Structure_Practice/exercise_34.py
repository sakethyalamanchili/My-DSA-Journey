"""
Problem: Merge Dictionaries with Overlapping Keys

Description:
    Design a Python function named merge_dicts_with_overlapping_keys that merges 
    multiple dictionaries into a single dictionary. 
    If a key appears in more than one dictionary, sum up their values.

Input Parameters:
    dicts (List[dict]): A list of dictionaries where keys might overlap.

Output:
    dict: A single dictionary where values for overlapping keys are summed.

Examples:
    Input: [{'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {'c': 5, 'd': 6}]
    Output: {'a': 1, 'b': 5, 'c': 9, 'd': 6}
    # 'b' was 2 + 3 = 5
    # 'c' was 4 + 5 = 9

    Input: [{'x': 10, 'y': 20}, {'y': 30, 'z': 40}, {'z': 50, 'x': 60}]
    Output: {'x': 70, 'y': 50, 'z': 90}
"""

def merge_dicts_with_overlapping_keys(dicts):
    result = {}
    for d in dicts:
        for key, value in d.items():
            result[key] = result.get(key, 0) + value
    
    return result

print(merge_dicts_with_overlapping_keys([{'x': 10, 'y': 20}, {'y': 30, 'z': 40}, {'z': 50, 'x': 60}]))