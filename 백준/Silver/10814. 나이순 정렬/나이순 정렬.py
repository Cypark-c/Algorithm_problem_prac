'''
[아이디어]
그냥 나이 순 정렬이라 어렵지 않을듯
단, 나이가 같을 때 가입순으로? 이건 그냥 놔두면 안건드리나?
맞더라도 이 부분을 알고 가야할듯
'''

import sys
input=sys.stdin.readline
N=int(input())
names=[]
for _ in range(N):
    Age,name=input().split()
    Age=int(Age)
    names.append((Age,name))
names.sort(key=lambda x:x[0])
for i in range(N):
    print(names[i][0],names[i][1])