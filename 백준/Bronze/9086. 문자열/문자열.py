T = int(input())
S = [input() for _ in range(T)]
for s in S:
    print(s[0] + s[len(s) - 1])