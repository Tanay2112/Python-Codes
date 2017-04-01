def palindrome(s):
	if s==s[::-1]:
		return 1
	return 0
def symmetry(s):
	if len(s)%2==0:
		if s[0:len(s)//2]==s[len(s)//2:len(s)]:
			return 1
		return 0
	else:
		if s[0:len(s)//2]==s[len(s)//2+1:len(s)]:
			return 1
		return 0
n=int(input("Enter number of strings"))
l=[]
for i in range(n):
	l.append(input("Enter a string").lower().rstrip())
for i in range(n):
	c=palindrome(l[i])
	d=symmetry(l[i])
	if c==1 and d==1:
		print("Both property")
	elif c==1:
		print("Palindrome")
	elif d==1:
		print("Symmetry")
	else:
		print("No property")
