nums = [3,2,2,3,4,2]
val = 3
nums [:]= [i for i in nums if i != val]
print(len(nums), nums)

while val in nums :
	nums.remove(val)
print(len(nums), nums)
# Do upvote if its helpful,Thanks.