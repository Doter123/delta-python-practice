# https://leetcode.com/problems/search-insert-position/description/
# Найдите индекс числа на котором находиться 'target' в массиве 'nums'
# если его нет то (где/на каком индексе) он бы находился

nums = [1,3,5,6]
target = 2

def searchInsert(nums: [int], target: int) -> int:
    l = 0
    r = len(nums)
    while l < r:
        mid = (l + r) // 2
        if nums[mid] < target: l = mid + 1
        else: r = mid

    return l

print(searchInsert(nums, target)) # 1