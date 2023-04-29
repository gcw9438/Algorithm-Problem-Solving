N = list(map(int, input().split()))
for i in range(len(N) - 1):
    if N[i] + 1 == N[i+1]:
        result = "ascending"
    elif N[i] - 1 == N[i+1]:
        result = "descending"
    else:
        result = "mixed"
        break
print(result)