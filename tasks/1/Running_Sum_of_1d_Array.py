nums = [1,2,3,4]

result = []

sums = 0

for n in nums:
    sums += n
    result.append(sums)

print(result)

# ====================

result = []

i = 1

result.append(nums[0])
while i < len(nums):
    result.append(result[i - 1] + nums[i])
    i += 1


print(result)
