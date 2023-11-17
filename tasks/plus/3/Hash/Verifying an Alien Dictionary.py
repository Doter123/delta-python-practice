from typing import List

def isAlienSorted(words: List[str], order: str) -> bool:

    obj = {char:index for index,char in enumerate(order)}
    word_indexes = [[obj[char] for char in word] for word in words]
    return all(w_i1 <= w_i2 for w_i1, w_i2 in zip(word_indexes, word_indexes[1:]))

    # ===============================================================

    # ord_d = {c:i for i,c in enumerate(order)}

    # for w1, w2 in zip(words, words[1:]):
    #     for i, j in zip(w1, w2):
    #         if i != j:
    #             if ord_d[i] > ord_d[j]: return False
    #             break

    #     if w1.startswith(w2) and w1 != w2: return False

    # return True

    # ===============================================================

    # if len(words) < 2:
    #     return True

    # d = {c:i for i,c in enumerate(order)}
    # d["#"] = -1

    # for i in range(1, len(words)):
    #     w1 = words[i-1]
    #     w2 = words[i]
    #     l1 = len(w1)
    #     l2 = len(w2)

    #     if l1 < l2:
    #         w1 += '#' * (l2 - l1)
    #     else:
    #         w2 += '#' * (l1 - l2)

    #     for j in range(len((w1))):
    #         if w1[j] != w2[j]:
    #             if d[w1[j]] > d[w2[j]]: return False
    #             break
    # return True

print(isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz")) # True
print(isAlienSorted(["word","world","row"], "worldabcefghijkmnpqstuvxyz")) # False
print(isAlienSorted(["apple","app"], "abcdefghijklmnopqrstuvwxyz")) # False
