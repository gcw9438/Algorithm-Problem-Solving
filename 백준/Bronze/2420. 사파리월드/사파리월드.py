N, M = map(int, input().split())
if N < M:
    result = M - N
else:
    result = N - M
print(result)