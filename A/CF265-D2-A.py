path = input()
instructions = input()

j = 0
m = 1
for i in range(len(instructions)):
    if(path[j] == instructions[i]):
        m+=1
        j+=1

print(m)

# 124 ms 	0 KB 