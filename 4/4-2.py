N,X = (map(int,input().split()))
A = list(map(int,input().split())) 

for a in A:
  low = a<X
  if low is True:
    print(a,end=" ")
  else : pass
