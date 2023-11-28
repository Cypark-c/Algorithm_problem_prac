'''
[아이디어]
와 나도 구글 가고 싶다!
1. enter면 넣고, leave면 떠남.
2. 들어오는건 순서대로 리스트에 차곡차곡 넣으면 되는데 떠나는건 내맘대로
    - 그런데 일단은 들어와야만 떠나는게 가능.
    -반드시 스택 이나 큐라고 할 수는 없다. 왜냐면 떠나는건 순서가 없기 때문.
        → 그냥 리스트 사용 →실패!
* 추가:
    생각해보니 enter->leave->enter 이럴 수도 있긴 함 -_-
    보기보다 어려운데?
[복잡도]
시간초과가 뜨는데. 내 생각에 이건 출입 기록의 수 n이 10^6 까지 가기 때문에 그런 것 같음.
이거 빅-오로 O(n^2)만 가도 10^12라서 불가→2중 for문은 안됨
생각해보면 시간 복잡도를 줄일 수 있는게 해쉬 였던가? →해쉬 사용→dict 사용!
'''
import sys

input=sys.stdin.readline
N=int(input())
remnants=dict()
called_list=[]
for i in range(N):
    people,cmd=((input().rstrip()).split())
    if cmd=='enter':
        remnants[people]='enter'
        called_list.append(people) # 사람 이름을 저장해 두었다가 나중에 dict에서 호출할 것임
    else:
        remnants[people]='leave'

called_list=list(set(called_list)) # 설마 이것 때문에?
called_list.sort(reverse=True) # Wow..! 잘 기억하자

for item in called_list:
    if remnants[item]=='enter':
        print(item)
