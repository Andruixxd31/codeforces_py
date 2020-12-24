matrix = []
moves = 0

for i in range(5):
    line = input().split()
    for j in range(len(line)):
        if line[j] == '1':
            moves += abs(2 - int(i)) + abs(2 - int(j))

print(moves)

# 218 ms	0 KB
