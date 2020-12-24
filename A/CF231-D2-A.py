n = int(input())
solve = 0

for i in range(n):
    count = 0
    p = input().split()
    for letter in p:
        if letter == '1':
            count += 1
        if count == 2:
            solve += 1
            break

print(solve)

# 216 ms 0 KB
