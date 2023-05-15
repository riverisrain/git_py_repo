# 바구니 개수, 반복 횟수
number, replay = map(int, input().split())

basket=[0 for a in range(number)]

for a in range(replay):
    i,j,k = map(int, input().split())
    for num in range(i,j+1):
        basket[num-1]=k

for num in range(number):
    print(basket[num], end=' ')
