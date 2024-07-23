array = [1,2,3,4,5,6]
search = 4

def binary_search(array, search):
    low = 0
    high = len(array) - 1
    mid = 0
    while low <= high:
        mid = (low + high) // 2
        if array[mid] < search:
            low = mid + 1
        elif array[mid] > search:
            high = mid - 1
        else:
            return mid
    return -1

result = binary_search(array, search)
'''
Time Complexity:
    Best Case: O(1)
    Average Case: O(log n)
    Worst Case: O(log n)
Space Complexity:
    Iterative Implementation: O(n)
    Recursive Implementation: O(log n)
'''