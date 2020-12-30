v = list(map(int, input().split()))
n = input()

total = n.count('1') * v[0] + n.count('2') * v[1] \
    + n.count('3') * v[2] + n.count('4') * v[3]
print(total)

# 124 ms	300 KB
