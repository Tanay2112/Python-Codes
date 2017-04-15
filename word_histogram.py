from pprint import pprint
s = list(input('Enter a word: ').rstrip().lower())
data = {}
for i in s:
    data[i] = s.count(i)
pprint(data)
c = set(data.values())
invdic = {}
for i in c:
    invdic[i] = []
    for j,k in data.items():
        if k == i:
            invdic[i].append(j)
    invdic[i]=sorted(invdic[i])
    

##sorted(invdic)
pprint(invdic)
