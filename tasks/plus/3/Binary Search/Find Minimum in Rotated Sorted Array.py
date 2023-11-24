from typing import List

def findMin(nums: List[int]) -> int:

    l = 0 
    r = len(nums)-1
    res = float('inf')

    while l <= r:
        mid = (l + r)//2

        if nums[l] <= nums[mid]:
            res = min(res, nums[l])
            l = mid + 1
        else:
            res = min(res, nums[mid])
            r = mid - 1

    return res

print(findMin([3,4,5,1,2])) # 1
print(findMin([4,5,6,7,0,1,2])) # 0
print(findMin([11,13,15,17])) # 11