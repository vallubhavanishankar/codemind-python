def reverse(n):
    return int(str(n)[::-1])
def ispalindrome(n):
    if(n==reverse(n)):
        return 1
    else:
        return 0
x=int(input())
x += reverse(x)
while(ispalindrome(x) != 1):
    x+=reverse(x)
print(x)
