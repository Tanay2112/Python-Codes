from pprint import pprint
s = list(input('Enter a word: ').rstrip().lower())
c=0
for i in range(0,len(s)):
    if not s[i].isalpha():
        c=1
if c==0:
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
    pprint(invdic)
else:
    print("Invalid input")
