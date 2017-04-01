name=[]
while True:
    print("enter name")
    s=input()
    if s=='stop':
        break
    name.append(s)
print("number of friends ",len(name))
large=name[0]
for i in range(0,len(name)):
    if len(large)<len(name[i]):
        large=name[i]
print("name with longest length ",large)
print("number of characters ",len(large))
