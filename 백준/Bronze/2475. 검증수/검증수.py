def square(n):
    return int(n) ** 2

N = list(map(square, input().split()))
print(sum(N) % 10)