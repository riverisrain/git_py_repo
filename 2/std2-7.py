diceA, diceB, diceC=map(int, input().split())

if(diceA==diceB):
    if(diceA==diceC):   # a=b=c 3개 같을 때
        print(10000+(diceA*1000))
    else:       # a=b 2개가 같을 때
        print(1000+(diceA*100))

elif(diceA==diceC): # a=c 2개가 같을 때
    print(1000+(diceA*100))

elif(diceB==diceC):  # b=c 2개가 같을 때
    print(1000+(diceB*100))

#
else:
    if(diceA>diceB):
        if(diceC>diceA): # c가 가장 클 때
            print(diceC*100)
        else:           # a가 가장 클 때
            print(diceA*100)

    elif(diceB>diceC):      # b가 가장 클 때
        print(diceB*100)

    else:
        print(diceC*100)               
        

    

