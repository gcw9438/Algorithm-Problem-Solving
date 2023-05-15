N, M = map(int, input().split())
six_prices = []
one_prices = []
for _ in range(M):
    a, b = map(int, input().split())
    six_prices.append(a)
    one_prices.append(b)

six_min_price = min(six_prices)
one_min_price = min(one_prices)
result = 0

if six_min_price <= one_min_price * 6:
    result = six_min_price * (N // 6) + one_min_price * (N % 6)
    if six_min_price < one_min_price * (N % 6):
        result = six_min_price * (N // 6 + 1)
else:
    result = one_min_price * N

print(result)