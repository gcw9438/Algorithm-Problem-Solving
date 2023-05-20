N = int(input())
data = []
ans = []
for _ in range(N):
    x, y = map(int, input().split())
    data.append((x, y))
for i in data:
    cnt = 0
    for j in data:
        if i[0] < j[0] and i[1] < j[1]: 
            cnt += 1
    ans.append(cnt + 1)
for a in ans:
    print(a, end=' ')