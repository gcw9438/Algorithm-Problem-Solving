A, B = map(int, input().split())

count = 1
while True:
    if str(B)[len(str(B)) - 1] == '1':
        B = int(str(B)[:-1])
        count += 1
    elif B % 2 == 0:
        B = B // 2
        count += 1
    elif not B % 2 == 0:
        count = -1
        break
    if B == A:
        break
    elif B < A:
        count = -1
        break

print(count)