len=int(input())
A = list(map(int,input().split())) 
max=A[0]
min=A[0]

for i in range(0,len):
    if A[i]>max:
        max=A[i]
    elif A[i]<min:
        min=A[i]

print(min, max)