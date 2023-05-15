# 바구니 개수, 반복 횟수
number, replay = map(int, input().split())

basket=[i for i in range(1,number+1)]
temp = 0

for i in range(replay):
    i,j=map(int,input().split())
    temp=basket[i-1]
    basket[i-1]=basket[j-1]
    basket[j-1]=temp

for i in range(number):
    print(basket[i], end=' ')
