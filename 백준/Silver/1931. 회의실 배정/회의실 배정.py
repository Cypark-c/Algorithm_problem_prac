import sys
input=sys.stdin.readline
# 회의실 배정하기
# 힌트가 튜플같음
N=int(input())
S_list=[]# 스케쥴을 담을 리스트
for _ in range(N):
    S_list.append(tuple(map(int,input().split())))

'''
최대한 많은 회의의 수를 배정해야 하는데, 회의는 겹치지 안항야 하고
1. 끝나는 것과 동시에 다음 회의 시작 가능
2. 회의의 시작시간 끝나는 시간 같을 수 있음
'''

'''
예를 들어 시작이 0면 (0,6)말고 선택지가 없다.
다음 회의 시간은 6부터 시작이 가능하다.
그 상황에서 선택지는 (6,10) 뿐 마찬가지의 방식으로 그 이후 선택지는 (12,14)

다음 결론을 내릴 수 있다. 
1.시작 시간이 최대한 빠른게 좋고,
2.종료 시간이 최대한 빠른게 좋다.
그 중에서도 우선 2번이 최우선이다. 시작시간이 좀 느려도 더 빨리 끝나면 좋다.
'''
S_list.sort(key=lambda x:x[0])
S_list.sort(key=lambda x:x[1])

cnt=1 # 배정할 수 있는 회의실 수
idx=0 # 순회하면서 도는 인덱스
compare_idx=idx+1
while(compare_idx<N):

    if S_list[idx][1]<=S_list[compare_idx][0]:
        cnt+=1
        idx=compare_idx
        compare_idx=idx+1
    else:
        compare_idx+=1
print(cnt)

# 그런데 좀 더 깔끔하게 풀어야 할텐데..
