from typing import List

def maxProduct(nums: List[int]) -> int:
    current_max, current_min = nums[0], nums[0]
    product = nums[0]

    for num in nums[1:]:
        values = (
            num,
            num * current_max,
            num * current_min
        )
        current_max, current_min = max(values), min(values)

        product = max(product, current_max)

    return product

    # if len(nums)==1:
    #     return nums[0]
    # l, r = 1, 1
    # maxx = 0
    # for i in range(len(nums)):
    #     l *= nums[i]
    #     r *= nums[len(nums)-1-i]
    #     maxx = max(maxx, l, r)
    #     l = 1 if l == 0 else l
    #     r = 1 if r == 0 else r

    # return maxx

print(maxProduct([2,3,-2,4])) # 6
print(maxProduct([-2,0,-1])) # 0
print(maxProduct([-2,3,-4])) # 24