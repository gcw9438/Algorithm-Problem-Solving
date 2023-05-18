T = int(input())
results = []
for _ in range(T):
    H, W, N = map(int, input().split())
    if N % H == 0:
        result = str(H) + "{:02d}".format(N // H)
    else:
        result = str(N % H) + "{:02d}".format((N // H) + 1)
    results.append(result)

for r in results:
    print(r)