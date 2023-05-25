data = []
for _ in range(9):
    data.append(int(input()))
total = sum(data)
h1, h2 = (0, 0)
for i in range(9):
    for j in range(i + 1, 9):
        if total - data[i] - data[j] == 100:
            h1, h2 = data[i], data[j]
            break

data.remove(h1)
data.remove(h2)
data.sort()
for i in data:
    print(i)