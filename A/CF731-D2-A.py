w = input()
w = 'a' + w
total = 0


for i in range(len(w) - 1):
    total += \
        min(abs(ord(w[i]) - ord(w[i + 1])),
            26 - abs(ord(w[i]) - ord(w[i + 1])))

print(total)

# 109 ms	0 KB
