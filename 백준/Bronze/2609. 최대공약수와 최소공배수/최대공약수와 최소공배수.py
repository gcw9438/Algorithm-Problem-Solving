N, M = map(int, input().split())
A = N
B = M
while B != 0:
    C = A % B
    A = B
    B = C
print(A) # 최대공약수
print((N * M) // A) # 최소공배수