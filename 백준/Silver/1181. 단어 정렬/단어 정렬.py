'''
[아이디어]
-길이가 짧은것?→len
-사전순?->길이가 같을때 비교를 해야 할 것 같다.
    - a~z까지 들어가는데 흠.. 아스키로 반환 가능하지 않나?
    - 이 함수가 얼마나 자주 쓰이는지는 모르겠는데 ord 함수가 있었음.

-일단 받으면 리스트에 넣어야 할 것 같은데
    1. 길이가 최우선
    2. 주어지는 문자열의 길이가 최대 50? → index 0~51까지 선언
        - 이렇게 하면 일단 길이만으로는 정렬이 가능.
        - 그리고 같은 길이 내에서는 sort를 하면 될 것 같은데?
[복잡도]
- 일단 받으면 리스트에 넣어야 할 것 같은데
- 리스트는 길이 51(index 0까지 고려함)
- nlogn이 n칸 →(n**2)logn 인데 좀 아슬아슬해보임
[변수]
'''
import sys
input=sys.stdin.readline
N=int(input())
dicti_list=[[] for _ in range(51)] # 2차원 배열, 0~50행 선언, 0행에는 아무것도 안들어 갈 것
for _ in range(N):
    word=input().rstrip()
    index=len(word)
    if word not in dicti_list[index]:
        dicti_list[index].append(word)

for i in range(1,51): # 범위 실수 했었던 듯 주의!
    if dicti_list[i]!=[]: # 이 표현이 간단하긴 한데 마음에 안든다! 싫음
        dicti_list[i].sort()
        for word in dicti_list[i]:
            print(word)