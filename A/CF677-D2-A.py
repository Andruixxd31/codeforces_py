n, h = map(int, input().split())
sum = 0

x = list(map(int, input().split()))
for y in x:
    if y <= h:
        sum += 1
    else:
        sum += 2

print(sum)

# 109 ms	300 KB
