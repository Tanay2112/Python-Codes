##def pan(s):
##    l=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
##    flag=0
##    for i in l:
##        if i not in s:
##            flag=1
##            break
##    return flag
##word=input("Enter a string")
##a=pan(word)
##if a==0:
##    print("Pangram")
##else:
##    print("Not pangram")
def pan(s):
    if len(s)>=26:
        return 1
    else:
        return 0
word=set(input("Enter a string"))
if pan(word)==1:
    print("Pangram")
else:
    print("Not")
