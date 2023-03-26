N=int(input())
ropes = []
for _ in range(N):
    ropes.append(int(input()))
ropes.sort()
W = []
for i in ropes:
    W.append(i*N)
    N-=1
print(max(W))