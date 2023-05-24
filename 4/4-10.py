count=int(input())
score=[]

score=list(map(int,input().split()))
maxx=max(score)

for i in range(0,count):
    score[i]=(score[i]/maxx*100)

average=sum(score)/count
print(average)
