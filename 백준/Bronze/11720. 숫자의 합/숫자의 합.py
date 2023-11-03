import sys
N=int(input())
numbers=list(map(int,sys.stdin.readline().rstrip()))
for i in range(1,N):
    numbers[i]+=numbers[i-1] # 아마 이게 sum 연산보다 시간이 빠를 것
print(numbers[N-1])