# 일반적인 접근
- Greedy 문제의 연습은, 우선 다른 접근에 대해 생각을 해보고 그게 안될 것 같으면 그리디로 돌아와서 연습하는 방식이 도움이 된다.
  - 따라서 먼저 다른 접근방법을 생각해 보다가 풀이를 떠올리게 되는게 보통이다.

# 1931번 접근

[전략구상]
- 스케쥴링 할 때, 어떻게 할지 고민을 하다가, 어쨌든 회의가 빨리 끝나면 이득이므로, 
  회의를 빨리 끝나게 만들려면, 주어진 튜플에서 종료시간을 오름차순으로 sorting 하는게 좋다고 생각이 된다.

[주의할점]
- 이 문제의 경우 회의가 
  (2,2)
  (1,2)
  위와 같은 케이스를 주의해야 한다.
  회의실 배정이 (1,2)도 충분히 할 수 있음에도 (2,2)를 선택해 버리면, 우리가 정한 그리디 알고리즘으로는 (1,2)를 잡아내지 못한다.
  그렇기 때문에 먼저 시작시간 기준으로 정렬 후에, 종료시간을 정렬해야한다.
</p>
