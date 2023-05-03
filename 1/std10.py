num1=int(input())
num2=int(input())
temp=num2

b1=num2//100
num2-=b1*100
b2=num2//10
num2-=b2*10
b3=num2

print(num1*b3)
print(num1*b2)
print(num1*b1)
num2=temp
print(num1*num2)