N = int(input())
schedule = []
cnt = 1
for _ in range(N):
    start, end = map(int, input().split())
    schedule.append((start, end))
schedule.sort(key = lambda x:x[0])
schedule.sort(key = lambda x:x[1])
tmp = schedule[0]
for i in range(1, N):
    if tmp[1] <= schedule[i][0]:
        cnt += 1
        tmp = schedule[i]
print(cnt)