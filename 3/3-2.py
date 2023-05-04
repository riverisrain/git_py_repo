number=int(input())
list=[]

for i in range(1,number+1):

    A, B=map(int, input().split())
    list.append(A+B)

for j in range(0,number):
    print(list[j])
