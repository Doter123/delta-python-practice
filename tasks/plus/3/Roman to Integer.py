# От римского к целому числу

def romanToInt(s: str) -> int:
    m = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    ans = 0
    # i = 0

    # while i < len(s):
    #     if i < len(s) - 1 and m[s[i]] < m[s[i+1]]:
    #         ans += m[s[i+1]] - m[s[i]]
    #         i += 2
    #     else:
    #         ans += m[s[i]]
    #         i += 1
    
    for i in range(len(s)):
        if i < len(s) - 1 and m[s[i]] < m[s[i+1]]:
            ans -= m[s[i]]
        else:
            ans += m[s[i]]
    
    return ans

print(romanToInt(""))  #  0
print(romanToInt("III"))  #  3
print(romanToInt("XIV"))  #  14
print(romanToInt("LVX"))  #  55
print(romanToInt("LVIII"))  #  58
print(romanToInt("MCMXCIV"))  #  1994