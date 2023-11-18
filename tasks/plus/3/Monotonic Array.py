from typing import List

def isMonotonic(nums: List[int]) -> bool:
    asc, desc = True, True

    for i in range(1, len(nums)):
        if nums[i-1] < nums[i]:
            desc = False
        if nums[i-1] > nums[i]:
            asc = False

    return asc or desc


print(isMonotonic([1,2,2,3])) # True
print(isMonotonic([6,5,4,4])) # True
print(isMonotonic([1,3,2])) # False