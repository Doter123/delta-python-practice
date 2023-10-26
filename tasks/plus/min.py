nums = [1,2,3,0,4,6,4,-1]

def get_min_number(nums):
    number = nums[0]
    i = 1

    while i < len(nums):
        if nums[i] < number:
            number = nums[i]
        i += 1

    return number

print(get_min_number(nums))