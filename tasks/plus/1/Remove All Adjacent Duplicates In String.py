# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

string = "abbaca"

result = []

for char in string:
    if result and result[-1] == char: # if current char is last result char
        result.pop() # remove this last char
    else:
        result.append(char)

print(''.join(result)) # ca