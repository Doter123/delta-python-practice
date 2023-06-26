haystack = 'bsadutsad'
needle = 'sad'
result = -1

print(len(haystack) - len(needle))

for i in range(len(haystack) - len(needle) + 1):
    if all(haystack[i + j] == needle[j] for j in range(len(needle))):
        result = i
        break

# result = haystack.find(needle)
print(result)


# nums = [1,3,5,6]
# target = 5
# result = -1

# result = haystack.find(needle)


# print(result)
