nums = [4,1,2,1,2]

obj = {}

for n in nums:
    if n in obj:
        obj[n] += 1
    else:
        obj[n] = 1

for i in obj:
    if obj[i] == 1:
        print(i)
        break
