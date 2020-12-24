word = input()
diff = 0

for i in word:
    if i.isupper():
        diff += 1
    else:
        diff -= 1

print(word.upper() if diff > 0 else word.lower())

# 218 ms	0 KB
