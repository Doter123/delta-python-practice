# https://leetcode.com/problems/search-insert-position/description/

nums = [1,3,5,6]
target = 2


result = -1
i = 0

while i < len(nums) - 1:
    if nums[i] == target:
        result = i
        break
    elif nums[i] < target and target < nums[i + 1]:
        result = i + 1
        break
    i += 1

print(result)

# ==================

nums.append(target)

nums.sort()

result = -1
i = 0

while i < len(nums):
    if nums[i] == target:
        result = i
        break
    i += 1

print(result)
