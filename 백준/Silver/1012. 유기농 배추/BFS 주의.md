## 주의점
def BFS...

  queue=deque()
  queue.append([r,c])

  while(1)
    graph[r][c]=0
    r,c=queue.popleft()
  
    for i in range(4):
      nr=r+dx[i]
      ny=c+dy[i]
      for (-1<nr<N and -1<nc<M) and not (graph[nr][nc]==0):
         graph[nr][nc]=0 # 이 방문 처리를 먼저 안한다?
         r,c=queue.popleft()

### 방문처리를 먼저 안하고 큐를 빼면 어떤일이 생기나?
[graph]
1 2
3 4
[1]
[1,2,3]
[2,3] 여기서 4를 방문을 해야하는데
★만약에 graph[nr][nc]=0 처리를 for문에서 처리하지 않고
그냥 while 문에서 graph[r][c]=0 이런식으로 해버리면
for 반복문에서 2번노드가 4번 노드를 방문 후에, 다시 3번노드가 4번 노드를 또 방문한다 
(왜냐하면 4라는 노드는 2번노드에서 방문을 하긴 했는데, 아직 for문 실행중이라서 3번노드에서 재차 방문해버리기 때문이다)
