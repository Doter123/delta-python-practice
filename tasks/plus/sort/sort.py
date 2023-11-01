nums = [1,2,3,0,4,6,4,-1]

def my_sort(nums):
    isSorted = True
    i = 0

    while i < (len(nums) - 1):
        if nums[i] > nums[i + 1]:
            first_num = nums[i]
            nums[i] = nums[i + 1]
            nums[i + 1] = first_num

            isSorted = False
        i += 1

    if isSorted:
        return nums
    else:
        return my_sort(nums)

print(my_sort(nums))