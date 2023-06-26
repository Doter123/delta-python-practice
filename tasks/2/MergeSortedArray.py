nums1 = [1,2,3,0,0,0,0,-1]
m = 3
nums2 = [0,5,6,4]
n = 4

# result = nums1
# for i,num in enumerate(result):
#     if i == (m + n):
#         break
#     if i >= m:
#         nums1[i] = nums2[i - m]
#     else:
#         nums1[i] = num
        
# nums1.sort()

# print(nums1)


for i in range(m, m+n):
    nums1[i] = nums2[i - m]
        
nums1.sort()

print(nums1)