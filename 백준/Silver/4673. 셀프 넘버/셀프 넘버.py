def d(n):
    sum=n
    while n!=0:
        sum+=(n%10)
        n=n//10
    return sum

notSelfNum=[]

for n in range(1,10001):
    notSelfNum.append(d(n))

for n in range(1,10001):
    if n not in notSelfNum:
        print(n)