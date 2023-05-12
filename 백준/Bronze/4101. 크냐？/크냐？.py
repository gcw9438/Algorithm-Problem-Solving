results = []

while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    if A > B:
        results.append("Yes")
    else:
        results.append("No")

for result in results:
    print(result)