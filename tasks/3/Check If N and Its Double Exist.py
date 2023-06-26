arr = [10,2,5,3] # [3,1,7,11]

result = False
temp_set = set()

for n in arr:
    if n * 2 in temp_set or n / 2 in temp_set:
        result = True
    temp_set.add(n)

print(result)