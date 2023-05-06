N = int(input())
cnt = 1
titleNum = 666
while cnt < N:
    titleNum += 1
    if "666" in str(titleNum):
        cnt += 1
print(titleNum)