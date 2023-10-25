def solution(my_string, target):
    

    # target의 길이가 주어질 것
    # Apple ppl
    # len(Appleman)=8, index 0,1,2,3,4,5,6,7 
    # len(ppl)=3, index 0,1,2
    
    
    if len(target)>len(my_string):
        return 0
    
    for i in range(len(my_string)-len(target)+1):
        if my_string[i:i+len(target)]==target:
            return 1  
    return 0