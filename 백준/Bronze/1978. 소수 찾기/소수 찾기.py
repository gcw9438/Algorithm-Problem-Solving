N = int(input())
nums = list(map(int, input().split()))
cnt = 0
for n in nums:
    if n == 1:
        continue
    primeNumCheck = True
    for i in range(2, n):
        if n % i == 0:
            primeNumCheck = False
            break
    if primeNumCheck == True:
        cnt += 1
print(cnt)
