# Надо найти самую среднюю (сумму k чисел разделённое на k`)

nums = [1,3,12,-5,-6,50]
k = 4

k_sums = []

for i in range(len(nums) - (k - 1)):
    k_sum = 0
    for j in range(k):
        k_sum += nums[i + j]
    k_sums.append(k_sum / k)

print(max(k_sums))

# Output: 12.75
# Explanation: Maximum average is  ->  ((12 - 5 - 6 + 50) / 4)   =   (51 / 4)   =   (12.75)