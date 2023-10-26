word = "abc"
string = "ahbgdc"

for character in string:
    if word != '' and character == word[0]:
        word = word[1:]
    if len(word) == 0:
        break

print(len(word) == 0)