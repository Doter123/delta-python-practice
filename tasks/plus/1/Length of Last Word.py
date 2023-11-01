# https://leetcode.com/problems/length-of-last-word/description/

string = "   fly me   to   the moon  "

i = len(string) - 1

result = ''

while i >= 0:
    if string[i] != ' ':
        result += string[i]
    elif result != '':
        break
    i -= 1

print(len(result))