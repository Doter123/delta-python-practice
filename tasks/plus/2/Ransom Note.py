from collections import Counter

def canConstruct(ransomNote: str, magazine: str) -> bool:
    cnt_r = Counter(ransomNote)
    cnt_m = Counter(magazine)

    for k,v in cnt_r.items():
        if cnt_m[k] < v:
            return False

    return True


print(canConstruct("a", "b")) # False
print(canConstruct("aa", "ab")) # False
print(canConstruct("aa", "aab")) # True