"""
Problem: Count Word Frequency

Description:
    Design a Python function named count_word_frequency to count the frequency 
    of words in a sentence and store the counts in a dictionary.

Input Parameters:
    sentence (str): The input sentence to analyze.

Output:
    dict: A dictionary where keys are words and values are their frequencies.

Examples:
    Input: "hello world hello"
    Output: {'hello': 2, 'world': 1}

    Input: "the quick brown fox jumps over the lazy dog"
    Output: {'the': 2, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, ...}
"""

def count_word_frequency(sentence):
    words = sentence.split()
    frequency = {}
    
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    
    return frequency

print(count_word_frequency("hello world hello"))