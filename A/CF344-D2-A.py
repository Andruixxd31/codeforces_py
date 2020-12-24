n = int(input())
last = 2
g = 0

for i in range(n):
    num = int(input())
    if num != last:
        g += 1
        last = num

print(g)

# 466 ms	0 KB
