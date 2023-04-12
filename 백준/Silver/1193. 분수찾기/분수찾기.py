N = int(input())

line = 0
end_N = 0
while N > end_N:
    line += 1
    end_N += line

if line % 2 == 0:
    print(f"{line - (end_N - N)}/{ end_N - N + 1}")
else:
    print(f"{ end_N - N + 1}/{line - (end_N - N)}")