s1 = input()
s2 = input()
count = 0

for i in range(len(s1)):
    if s1[i].lower() > s2[i].lower():
        count += 1
        break
    elif s1[i].lower() < s2[i].lower():
        count -= 1
        break

print(count)

# 186 ms	0 KB
