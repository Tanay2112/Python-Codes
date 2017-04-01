word=input("Enter a String ")
c=0
d=0
if word[0].isalpha():
    if len(word)>=8:
        for ch in word:
            if ch.isdigit():
                c=1
            elif not ch.isalpha():
                d=1
        if c==1 and d==1:
            print("valid")
        else:
            print("invalid")
    else:
        print("invalid")
else:
        print("invalid")
