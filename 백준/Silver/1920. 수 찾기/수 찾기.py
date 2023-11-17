'''
[아이디어]
- 그냥 제출했더니 시간 초과가 뜸. A리스트를 set로 바꿔보기
'''
import sys
input=sys.stdin.readline
N=int(input())
A_list=set(map(int,input().split()))
M=int(input())
M_list=list(map(int,input().split()))
for item in M_list:
    print(1) if item in A_list else print(0)