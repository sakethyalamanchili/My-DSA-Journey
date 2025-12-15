def linear_search(arr, target):
    for i, num in enumerate(arr):
        if target == num:
            return i
    return -1

print(linear_search([3, 7, 2, 5], 2))