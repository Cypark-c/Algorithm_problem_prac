# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 첫번재 풀이는 우선 아래와 같이 풀 수 있을 것 같다.
from itertools import permutations
N,M=map(int,input().split())
X=[i for i in range(1,N+1)]
pros=list(permutations(X,M))

for i in range(len(pros)):
    for j in range(0,len(pros[i])):
        print(pros[i][j],end=' ')
    print("")