result = []
while True:
    N = input()
    if N == '0':
        break
    if N == N[::-1]:
        result.append("yes")
    else:
        result.append("no")
for _ in result:
    print(_)