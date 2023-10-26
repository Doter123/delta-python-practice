nums1 = [1,2,3,0,0,0,0,-1]
start = 3
length = 4
nums2 = [0,4,6,4]

for i in range(length):
    nums1[i + start] = nums2[i]
        
nums1.sort()

print(nums1)




















