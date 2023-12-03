'''
난 솔직히 어려웠음
약간 복불복 문제 같아서 좀..
그러나 예외처리를 굳이 반복문을 돌면서 안해도 될 수 있다.
다 만들고 나서 해도 됨. ←이걸 생각하는게 어려운 문제
'''
def make_nums(pos,result):
    if pos==len(str(N)):
        if not '0' in str(result):
            result_lt.append(result)
        return

    for key in K_list:
        now=key*(10**(len(str(N))-(pos+1)))+result
        if now<=N:
            make_nums(pos+1,now)
        else:
            make_nums(pos+1,result)

import sys
input=sys.stdin.readline
result_lt=[]
N,K=map(int,input().split())
K_list=list(map(int,input().split()))
K_list.sort(reverse=True) # 큰 수부터 대입
make_nums(0,0)
print(max(result_lt))