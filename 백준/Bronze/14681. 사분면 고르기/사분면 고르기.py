X=int(input())
Y=int(input())
pos=-1
if X*Y>0:
    if X>0:
        pos=1
    else:
        pos=3
else:
    if Y>0:
        pos=2
    else:
        pos=4
print(pos)