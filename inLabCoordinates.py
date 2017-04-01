import math
x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())
if y1==y2:
    x=x2-x1
    x3=x1
    y3=y1+x
    x4=x2
    y4=y2+x
    d=math.sqrt(math.pow(x2-x1,2)+math.pow(y3-y1,2))
else:
    y=y2-y1
    y3=y1
    x3=x1+y
    y4=y2
    x4=x2+y
    d=math.sqrt(math.pow(x3-x1,2)+math.pow(y2-y1,2))
l1=(x3,y3)
l2=(x4,y4)
print(l1)
print(l2)
print(format(d,'.2f'))
