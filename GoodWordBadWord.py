word=input("enter a string")
c=0
for i in range(0,len(word)):
    for j in range(i+1,len(word)):
        if word[i]==word[j]:
            c=1
if c==1:
    print("Bad word")
else:
    print("Good word")
