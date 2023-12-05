# set의 중요성!
import sys
input=sys.stdin.readline

N=int(input())

numcards=set(map(int,input().split()))

M=int(input())
Finds=list(map(int,input().split()))
for item in Finds:
    if item in numcards:
        print(1,end=" ")
    else:
        print(0,end=" ")

