# Найдите пропущенное число (если в массиве его нет то она равна 'max(nums)+1')

from typing import List

def missingNumber(nums: List[int]) -> int:
    length = len(nums) + 1
    for num in range(length):
        if num not in nums: return num

    # - Explanation: sum(range(nums-length + 1)) - sum(nums)
    #return sum(range(len(nums)+1))-sum(nums)

    # - Explanation: set and range with length + 1 minus set(nums)
    #return list(set(range(len(nums)+1)) - set(nums))[0]

    # - Explanation: Gauss Summation Formula
    #n=len(nums)
    #return n*(n+1)//2-sum(nums)


print(missingNumber([3,0,1])) # 2
print(missingNumber([0,1])) # 2
print(missingNumber([9,6,4,2,3,5,7,0,1])) # 8
