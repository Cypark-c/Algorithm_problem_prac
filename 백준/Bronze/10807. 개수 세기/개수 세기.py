import sys

N=int(input())
X=list(map(int, sys.stdin.readline().split()))
Y=int(input())
count=0

for item in X:
    if item==Y:
        count+=1

print(count)