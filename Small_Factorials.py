t=int(input())
for i in range(1,t+1):
    n=int(input())
    fac=1
    for b in range(1,n+1):
        fac=fac*b
    print(fac)