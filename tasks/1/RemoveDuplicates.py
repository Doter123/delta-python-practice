nums = [1,1,2,3,3,4,5,5,5,5,6,7,8,8,9,10,10]


# result = set()

# for n in nums:
#     result.add(n)


# print(list(result))






i = 0
while i != len(nums) - 1:
    if nums[i] == nums[i + 1]:
        del nums[i]

    else:
        i += 1
    
print(len(nums), nums)