# string = ["h","e","l","l","o"]
string = ["H","a","n","n","a","h"]

def reverseString(s: [str]) -> None:
    l = 0
    r = len(s)-1
    while l <= r: # пробег с лево и право -> в центр
        s[l], s[r] = s[r], s[l] # swap
        l += 1
        r -= 1

reverseString(string)

print(string)
