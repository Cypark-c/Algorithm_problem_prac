import sys
input=sys.stdin.readline()
D_list=list(map(int,input.split()))

prize=0
if len(set(D_list))==1:
    prize=10000+(D_list[0])*1000
elif len(set(D_list))==3:
    prize=max(set(D_list))*100
else:
    if (D_list[0]==D_list[1]) or (D_list[0]==D_list[2]):
        prize=1000+(D_list[0])*100
    else:
        prize=1000+(D_list[1])*100
print(prize)