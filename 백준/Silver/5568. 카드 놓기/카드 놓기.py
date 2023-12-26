'''
[아이디어]
- 카드는 n장 여기서 k개를 선택
- 가로로 나란히 정수
- k개를 선택해서 만들 수 있는 정수.

ex) 1,2,12,1 중 2개를 선택해서 만든다면
1을 중복해서 나오는 11과
1,2,12 중 3P2로 만드는 케이스 6가지해서 총 7개

위와 같이 중복을 고려해야함. 카드를 만들어서 결과리스트에 추가를하고
이미 방문했으면 다시 방문하지 않는 식으로 풀어보기

지금 뭔가 크게 착각하는 부분이 있음 (가령 append의 리턴은 None인데 이걸 있다고 생각한다든지)
백트래킹 연습 많이 해야할 것 같음
'''

# Backtracking
# number_lt는 임시로 맡아두는 배열, v는 cardlist중 몇 번째 원소인가를 나타냄
# 백트래킹에서 찍는 방법을 좀 이상하게 하고 있는거 같음
# visited는 방문 여부를 체크하기 위함
def DFS_BT(String,count):
    # 종료 조건
    if count==k:
        # 결과 append
        if String not in result:
            result.append(String)
        return

    # 방문노드를 append했으면 방문하지 않은 곳 중에서 하나를 골라서 들어감
    for index in range(len(visited)):
        # 아직 방문하지 않은 노드면 방문
        if visited[index]==0:
            #String+=str(cardlist[index])
            String_new=String+str(cardlist[index])
            count+=1
            visited[index] = 1  # 1은 해당 노드를 방문했다는 의미
            DFS_BT(String_new,count)
            # 해당 노드는 방문했으면 다시 원복 시켜주어야 함
            visited[index]=0 # 원복
            count-=1

import sys
input=sys.stdin.readline
n=int(input())
k=int(input())
cardlist=[]
# 카드가 적혀있는 수
for _ in range(n):
    cardlist.append(int(input()))

result=[]
visited=[0]*n
DFS_BT('',0)

#print(result)
#print(len(result))
print(len(set(result)))