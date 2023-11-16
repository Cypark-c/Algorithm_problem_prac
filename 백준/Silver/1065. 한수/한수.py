'''
[아이디어]
이건 엄청 쉬움
공차가 하나 나올건데 각 자리수가 이걸 만족하는지 확인하면 된다.
'''
import sys
input=sys.stdin.readline
N=int(input())
count=0 # 한수의 수
for number in range(1,N+1):
    # 자릿수에 따른 공차 지정
    if len(str(number))>=2: # 자릿수가 2보다 크다면
        d=int(str(number)[1])-int(str(number)[0])
    else: # 자릿수가 1자리면
        d=0

    for j in range(0,len(str(number))-1):
        a=int(str(number)[j])
        b=int(str(number)[j+1])
        if b-a==d:
            continue
        else:
            count-=1 # 한수가 아닌 수는 제거함
            break # for 문 빠져나옴, 이걸 안하면 답이 이상하게 나올 것 조심..
    count+=1 # 한수가 아닌 수가 제거 되더라도 그걸 제거하는게 목적은 아님, 그냥 세지 않음, 한수가 아닌 수는 당연히 카운트 증가
print(count)