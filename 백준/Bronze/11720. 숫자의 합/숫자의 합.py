import sys
N=int(input())
numbers=sys.stdin.readline().rstrip()
tot=0
for i in range(0,N):
    tot+=int(numbers[i])
print(tot)