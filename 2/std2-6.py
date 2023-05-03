H, M=map(int,input().split())
time=int(input())

# 분이 60분 배수 라면
if((M+time)%60==0):
    H=H+((M+time)//60)
    if(H>=24):
        H-=24
    M=0

# 분이 60을 넘으면
elif((M+time)>60):
    H=H+((M+time)//60)
    if(H>=24):
        H-=24

    M=(M+time)%60
   

# 분이 60을 안넘으면
else:    
    M=M+time

print(H, M)


