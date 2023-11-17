# Given an array of integers arr, return true if and only if it is a valid mountain array.

# Recall that arr is a mountain array if and only if:

# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1


from typing import List

def validMountainArray(arr: List[int]) -> bool:
    if len(arr) < 3: return False
    i = 0
    while i < len(arr) - 1 and arr[i] < arr[i+1]:
        i += 1
    j = len(arr) - 1
    while j > 0 and arr[j - 1] > arr[j]:
        j -= 1

    return i == j and 0 < i < len(arr) - 1

print(validMountainArray([2,1])) # False
print(validMountainArray([3,5,5])) # False
print(validMountainArray([0,3,2,1])) # True
print(validMountainArray([2,0,2])) # False
print(validMountainArray([0,1,2,3,4,5,6,7,8,9])) # False
print(validMountainArray([9,8,7,6,5,4,3,2,1,0])) # False