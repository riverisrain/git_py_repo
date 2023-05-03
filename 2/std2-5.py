H, M=map(int,input().split())
#M=int(input())

# 분이 45분보다 작을 때
if(M<45):
    if(H>=1):
        H-=1
    else:
        H=23
    
    M=45-M
    M=60-M
# 분이 45분보다 클 때
else:    
    M=M-45

print(H, M)
