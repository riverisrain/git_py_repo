total=int(input())
count=int(input())
sum=0

for i in range(0,count):
    price, number = map(int, input().split())
    sum=sum+(price*number)

if(sum==total):
    print("Yes")
else:
    print("No")