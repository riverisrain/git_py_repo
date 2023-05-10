number=int(input())

for i in range(1,number+1):
    str="*"*i
    print(str.rjust(number))