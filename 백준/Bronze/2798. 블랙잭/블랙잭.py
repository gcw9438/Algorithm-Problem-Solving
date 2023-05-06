N, M = map(int, input().split())
cards = list(map(int, input().split()))
result = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            cards_sum = cards[i] + cards[j] + cards[k]
            if cards_sum > M:
                continue
            else:
                result = max(result, cards_sum)
print(result)