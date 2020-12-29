n = int(input())
cards = list(map(int, input().split()))
sereja = 0
dima = 0


for i in range(n):
    if i % 2 == 0:
        sereja += cards.pop() if cards[0] < cards[len(cards) -
                                                  1] else cards.pop(0)
    else:
        dima += cards.pop() if cards[0] < cards[len(cards) -
                                                1] else cards.pop(0)

print(f'{sereja} {dima}')

# 108 ms	300 KB
