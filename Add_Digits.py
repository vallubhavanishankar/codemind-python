def add_digits(num):
    while num>=10:
        count=0
        num_str=str(num)
        for digit in num_str:
            count+=int(digit)
            num=count
    return count
    
num=int(input())
result=add_digits(num)
print(result)