lengthList = []
while True:
    N = input()
    if N == '0':
        break
    N = '_' + '_'.join(list(N)) + '_'
    length = 0
    for c in list(N):
        if c == '_':
            length += 1
        elif c == '1':
            length += 2
        elif c == '0':
            length += 4
        else:
            length += 3
    lengthList.append(length)

for l in lengthList:
    print(l)