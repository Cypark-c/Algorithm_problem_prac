from itertools import combinations 
# itertool 연습할 필요 있는듯 이거 모르면 귀찮게 조합 뽑아내야함

N,M=map(int,input().split()) # 카드의 개수와 딜러가 외친 수

Card_list=list(map(int,input().split()))
# 해당 카드 리스트는 적어도 3장 이상임.

comb_list=list(combinations(Card_list,3))
# 튜플로 반환되는 조합임

dif=M # 초기 차이 값을 설정함
su_three=0 # 초기 조합값의 합을 설정함
for comb in comb_list:
    if (sum(comb)<=M)&((M-sum(comb))<dif):
        dif=M-sum(comb) # dif 갱신
        su_three=M-dif

print(su_three)