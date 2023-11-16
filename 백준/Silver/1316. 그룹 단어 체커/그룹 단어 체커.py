'''
[아이디어]
- 열고 닫고 이런 식으로 가면 문제 없을 듯
- 어떤 글자가 나오면, 일단 이걸 켜놓음 (자리별 스위치를 카운팅 한다고 생각하기)
- 각 스위치 별로 현재 상태와 이전 상태를 비교해서 같다면 카운트를 하지 않음
    - 다시 같은 글자가 나타나면 카운트
    - 이 로직이면 어느 한 자리든 카운트가 2 이상인게 나오면 그룹 단어가 아님
    - 그렇다는 건 스위치를 set으로 만들었을 때 내가 기대하는 값이 전부 1이어야 그룹단어
[복잡도]
'''
import sys
input=sys.stdin.readline
N=int(input())
group_words=0
for _ in range(N):
    word=input().rstrip()
    char_list=list(set(word)) # word를 집합으로 받음 그 후 리스트 메서드 사용하기 위해 다시 리스트화
    switch=[0 for _ in range(len(char_list))] # char_list 즉, 집합 길이 만큼 스위치 선언
    switch[char_list.index(word[0])]=1 # 첫 글자는 초기화 해야함
    for i in range(0,len(word)-1):
        if word[i]==word[i+1]: # 다음 글자가 같다면
            continue # 컨티뉴, 즉 스위치를 올리지 않음
        else: # 다음 글자가 다르다면
            switch[char_list.index(word[i+1])]+=1 # 다음 글자가 포함된 char_list의 인덱스를 스위치에 넣어 올려줌
    if set(switch)=={1}: # 그룹단어라면
        group_words+=1
    # char_list나 switch를 보면서 디버깅해도 됨
print(group_words)