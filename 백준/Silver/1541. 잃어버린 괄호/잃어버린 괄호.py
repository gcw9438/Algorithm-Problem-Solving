mathExp = input() + ' '
num = ""
result = 0
isMinus = False
for i in range(len(mathExp)):
    if mathExp[i] == '+' or mathExp[i] == '-' or mathExp[i] == ' ':
        if isMinus:
            result -= int(num)
            num = ""
        else:
            result += int(num)
            num = ""
    else:
        num += mathExp[i]
    
    if mathExp[i] == '-':
        isMinus = True    
print(result)