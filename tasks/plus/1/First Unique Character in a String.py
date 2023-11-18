from collections import Counter

def firstUniqChar(s: str) -> int:
    cnt = Counter(s)

    for i, char in enumerate(s):
        if cnt[char] == 1:
            return i

    return -1

print(firstUniqChar("leetcode")) # 0
print(firstUniqChar("loveleetcode")) # 2
print(firstUniqChar("aabb")) # -1