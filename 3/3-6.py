import sys
list=[]
number=int(input())
number<=1000000

for i in range(0,number):
    A, B= map(int, sys.stdin.readline().split())
    print(A+B)