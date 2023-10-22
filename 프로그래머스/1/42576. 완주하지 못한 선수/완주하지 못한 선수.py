def solution(participant, completion): 

    # 우선 sort 시킴
    participant.sort()
    completion.sort()  
    
    # print('----')
    # print(participant)
    # print(completion)
    # print('----')
        
    answer=0
    # participant는 반드시 1명이 completion 보다 많음
    # 그냥 사람 1명이 더 많거나 ->remove로 값을 지우려니까 시간초과, 다른 방법 필요
    # 동명이인으로 1명이 더 많거나    
    
    for i in range(len(completion)):  
        if participant[i]!=completion[i]:
            answer=participant[i]
            # print(answer)
            return answer
    
    # print(participant[len(participant)-1])
    return participant[len(participant)-1]

 