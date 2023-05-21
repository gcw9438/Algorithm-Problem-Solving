T = int(input())
results = []
for _ in range(T):
    data = []
    k = int(input())
    n = int(input())
    for floor in range(k + 1): # 0 ~ k
        sum = 0
        if floor == 0:
            for i in range(1, n + 1): # 1 ~ n
                data.append(i)
        else:
            for i in range(1, n + 1):
                sum += data[i - 1]
                data[i - 1] = sum
    results.append(data[n - 1])
for r in results:
    print(r)