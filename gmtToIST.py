day=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
d=input("Enter day ")
h=int(input("Enter Hours in GMT "))
m=int(input("Enter Minutes in GMT "))
if 0<=h<24 and 0<=m<60 and d in day:
        m=m+30
        if m>60:
                m=m-60
                h=h+1
        h=h+5
        if h>23:
                h=h-24
                if d=='Saturday':
                        d=='Sunday'
                else:
                        for i in range(len(day)):
                                if d==day[i]:
                                        p=i+1
                        d=day[p]
        print("IST")
        print(d)
        print(h)
        print(m)
else:
        print("Invalid input")
