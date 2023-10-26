strings = ["flower","flow","flight"]

short = min(strings, key=len)

for item in strings:

    while len(short) > 0:

        if item.startswith(short):
            break
        else:
            short = short[:-1]

print(short)