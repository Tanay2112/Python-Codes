f=[]
a=[]
I=[]
t=[]
n=int(input())
for i in range(n):
	f.append(int(input()))
	a.append(int(input()))
	I.append(int(input()))
	t.append(f[i]+a[i]+I[i])
for i in range(n):
	k=t[i]
	c=i-1
	while c>=0:
		if t[c]<k:
			t[c+1]=t[c]
		else:
			break
		c=c-1
	t[c+1]=k
print(t)
