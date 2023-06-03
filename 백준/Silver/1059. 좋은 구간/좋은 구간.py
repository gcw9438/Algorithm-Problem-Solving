L = int(input())
S = list(map(int, input().split()))
n = int(input())

S.append(0)
S.sort()

ans = 0
for i in range(len(S) - 1):
    if S[i] == n or S[i+1] == n:
        ans = 0
        break
    elif S[i] < n and n < S[i+1]:
        ans = (n - S[i]) * (S[i+1] - n) - 1
        break

print(ans)