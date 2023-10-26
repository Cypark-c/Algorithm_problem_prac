
def solution(code):
    ret=''
    mode=0 # mode 시작조건 설정에 유의
    for idx,val in enumerate(code):
        if ((val)!='1'):       
            if (mode==0)&(idx%2==0):
                ret+=code[idx]
            elif (mode==1)&(idx%2==1):
                ret+=code[idx]    
        
        else:
            mode=(mode+1)%2
    
    if ret=='':
        return "EMPTY"
    
    return ret
