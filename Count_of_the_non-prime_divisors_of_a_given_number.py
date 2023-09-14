def isprime(d):
    if d==2:
        return 1
    for i in range(2,d//2+1):
        if d%i==0:
            return 0
    return 1
n=int(input())
count=0
for i in range(1,n+1):
    if n%i==0:
        if isprime(i)==0:
            count+=1
print(count + 1)
    