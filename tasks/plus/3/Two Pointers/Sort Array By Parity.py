from typing import List

def sortArrayByParity(nums: List[int]) -> List[int]:
    # l, r = 0, len(nums) - 1

    # while l <= r:

    #     if nums[l] % 2 == 0:
    #         l += 1
    #         continue
    #     if nums[r] % 2 != 0:
    #         r -= 1
    #         continue

    #     nums[l], nums[r] = nums[r], nums[l]

    #     l += 1
    #     r -= 1
    
    j = 0

    for i in range(len(nums)):

        if nums[i] % 2 == 0:
            nums[j], nums[i] = nums[i], nums[j]
            j += 1

    return nums

print(sortArrayByParity([3,1,2,4])) # [4,2,1,3]
print(sortArrayByParity([1,8,2,7,3,1,4,5,8,6,7])) # [6, 8, 2, 8, 4, 1, 3, 5, 7, 1, 7]
print(sortArrayByParity([0])) # [0]