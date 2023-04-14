N = int(input())
result = 1
if N != 0:
    for _ in range(N):
        result *= N
        N -= 1
print(result)