word = "acbi"
string = "ahbgdcopi"

for character in string:
    if word == '':
        break
    if character == word[0]:
        print('word =', word)
        word = word[1:]
        print('word =', word)



print(len(word) == 0, word, len(word))