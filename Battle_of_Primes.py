def isprime(d):
    for i in range(2,d//2+1):
        if d%i==0:
            return 0
    else:
        return 1
n1=int(input())
n2=int(input())
for i in range(n1+n2+1,n1+n2+100):
    if isprime(i)==1:
        print(i-(n1+n2))
        break