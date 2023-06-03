L = int(input())
S = list(map(int, input().split()))
n = int(input())
cnt = 0
S.append(0)
S.sort()
for idx in range(len(S) - 1):
    if S[idx] < n < S[idx + 1]:
        arr = list(range(S[idx] + 1, S[idx + 1])) 
        for i in range(len(arr)):
            for j in range (i + 1, len(arr)):
                if arr[i] <= n <= arr[j]:
                    cnt += 1
        break
print(cnt)
