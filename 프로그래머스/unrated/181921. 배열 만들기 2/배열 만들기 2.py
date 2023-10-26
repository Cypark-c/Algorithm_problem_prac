from itertools import product # 중복조합

def solution(l, r):
    set=['0','5']
    result=[]
    combs=[]
    '''
    맨 앞자리가 5로 픽스 되면 나머진 조합임 예를 들어서
    세자리고 5로 백의 자리가 픽스되면
    5??
    ??에는 00 05 50 55 이렇게 조합을 짤 수 있음.
    r값 어떻게 기준을 세워야 하나?
    그냥, 일단 r이 가진 자릿수 l이 가진 자릿수 
    자릿수만 파악한 다음에 l,r로 필터링 하자.
    '''
    
    flaglist=[1,2,3,4,5]
    flag_r=0
    for item in flaglist:
        if r//(10**item)>=1:
            flag_r+=1
    print(flag_r)
    # flag_r 값이 곧 0과 5를 조합할 수 있는 자리가 됨.
    '''
    flag_r=1이면 기본적으로는 4개 조합이 가능
    ???=>00,05,50,55
    flag_r=2이면 기본적으로는 8개 조합이 가능.
    ???=>000,005,050,055,500,505,550,555 이렇게 나옴
    '''
    
    for i in product([0,5],repeat=flag_r+1):
        combs.append(i)
    print(combs)
    for comb in combs:
        value_sum=0
        for i in range(flag_r+1):
            value_sum+=comb[i]*(10**(flag_r-i))
            
        if (value_sum>=l)&(value_sum<=r):  
            result.append(value_sum)
    print(result)
    
    if result==[]:
        return [-1]
    
    return result
    