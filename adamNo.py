def rev(s):
    return s[::-1]
n=input()
a=rev(n)
a=str(int(a)**2)
a=rev(a)
if int(n)**2==int(a):
    print('Adam number')
else:
    print('Not an Adam number')
