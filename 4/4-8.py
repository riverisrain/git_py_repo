num=[]

for i in range(10):
    num.append(int(input()))
    num[i]=num[i]%42

numlist=set(num)
print(len(numlist))