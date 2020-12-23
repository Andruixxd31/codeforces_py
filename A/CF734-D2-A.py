
n = int(input())
games = input()
A = D = 0

for i in games:
    if i == 'A':
        A += 1
    else:
        D += 1


print("Anton" if A > D else "Danik" if D > A else "Friendship")

# 109 ms	200 KB
