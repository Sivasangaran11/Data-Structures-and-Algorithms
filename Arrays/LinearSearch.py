array =[1,2,3,4,5]
number = 3
def linearSearch(array, number):
    for i in range(len(array)):
        if array[i] == number:
            return i
    return -1

result = linearSearch(array, number)
'''
Time Complexity:
    Best Case: O(1) - When the number is present at the first index
    Worst Case: O(n) - When the number is not present in the array
Space Complexity:
    O(1)
'''