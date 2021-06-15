val = list(map(int, input().split(' ')))
num = val[0]
r = val[1]


i = 1
while(True):
    if(num * i % 10 == 0 or (num * i - r) % 10 == 0):
        break
    i+=1

print(i)
    
# 77 ms 	0 KB