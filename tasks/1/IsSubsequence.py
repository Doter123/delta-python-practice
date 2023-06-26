s = "abc"
t = "ahbgdc"

charArray = list(s)[::-1]

for i in t:
    if charArray and i == charArray[-1]:
        charArray.pop()
    if len(charArray) == 0:
        break

print(len(charArray) == 0)