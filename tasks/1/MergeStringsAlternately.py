word1 = "abc"
word2 = "pqr"

index_1, index_2 = 0, 0

result = ''

while index_1 < len(word1) or index_2 < len(word2):
    if index_1 < len(word1):
        result += word1[index_1]
    if index_2 < len(word2):
        result += word2[index_2]
    index_1 += 1
    index_2 += 1

print(result)