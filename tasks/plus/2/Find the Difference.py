from collections import Counter

s = "abcd"
t = "abcdet"

# ord('A') - вернёт Unicode символа -> 65
# chr(65) - вернёт символ по (введенному/переданному) Unicode'у

def findTheDifference(s: str, t: str) -> str:
        sm, sm1 = 0, 0

        for i in range(len(s)):
            sm+=ord(s[i])
            sm1+=ord(t[i])

        sm1+=ord(t[len(s)])

        return chr((sm1-sm))

print(findTheDifference(s, t))



# Short ================

print(list(
    (Counter(t) - Counter(s)).elements()
)[0])
