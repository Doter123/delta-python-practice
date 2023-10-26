word1 = "abc"
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

for i in range(max(len(word1),len(word2))):
    if i < len(word1):
        result += word1[i]
    if i < len(word2):
        result += word2[i]
    
print(result)