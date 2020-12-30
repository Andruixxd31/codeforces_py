n = int(input())
rocks = input()
count = 0

for i in range(len(rocks) - 1):
    if rocks[i] == rocks[i+1]:
        count += 1

print(count)

# 218 ms	0 KB
