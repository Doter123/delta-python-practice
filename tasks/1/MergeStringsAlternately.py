word1 = "abchgfdhgf"
word2 = "pqr"

i = 0
result = ''

while i < len(word1) or i < len(word2):

    if i < len(word1):
        result += word1[i]

    if i < len(word2):
        result += word2[i]

    i += 1

print(result)

# ===================

result = ""

maximum = max(len(word1),3)

for i in range(maximum):
    if i < len(word1):
        result += word1[i]
    if i < len(word2):
        result += word2[i]
    
print(result)