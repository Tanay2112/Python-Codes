word=input()
r1="qwertyuiop"
r2="asdfghjkl"
r3="zxcvbnm"
c=0
if word[0] in r1:
    for ch in word:
        if not ch in r1:
            c=-1
            break
elif word[0] in r2:
    for ch in word:
        if not ch in r2:
            c=-1
            break
else:
    for ch in word:
        if not ch in r3:
            c=-1
            break
if c==-1:
    print("no")
else:
    print("yes")
