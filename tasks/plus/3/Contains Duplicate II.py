from typing import List

def containsNearbyDuplicate(nums: List[int], k: int) -> bool:

    for i in range(len(nums) - k):
        for j in range(i+1, i + 1 + k):
            if nums[i] == nums[j]:
                return True

    return False

print(containsNearbyDuplicate([1,2,3,1], 3)) # True
print(containsNearbyDuplicate([1,0,1,1], 1)) # True
print(containsNearbyDuplicate([1,2,3,1,2,3], 2)) # False
print(containsNearbyDuplicate([99,99], 2)) # True