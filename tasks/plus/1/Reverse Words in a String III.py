string = "Let's take LeetCode contest"

words = string.split()

reversed_words = []

for word in words:
    reversed_words.append(word[::-1])

print(' '.join(reversed_words))

# ============== Short ==============

reversed_words = [word[::-1] for word in words]

print(' '.join(reversed_words))