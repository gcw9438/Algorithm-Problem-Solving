T = int(input())
N = 3
results = []
for _ in range(T):
    arr = list(map(int, input().split()))
    arr.sort()
    results.append(arr[len(arr) - N])
for result in results:
    print(result)