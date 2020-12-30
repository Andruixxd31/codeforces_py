n = int(input())
ev = list(map(int, input().split(' ')))
crimes = reserves = 0

for i in range(len(ev)):
    if ev[i] > 0:
        reserves += ev[i]
    else:
        if reserves == 0:
            crimes += 1
        else:
            reserves -= 1

print(crimes)

# 155 ms	5300 KB
