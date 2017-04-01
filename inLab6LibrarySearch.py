def bsearch(A,B,R,AccNo):
    if(A>B):
        return -1
    mid=(A+B)//2
    if AccNo[mid]==R:
        return mid
    if R>AccNo[mid]:
        return bsearch(mid+1,B,R,AccNo)
    else:
        return bsearch(A,mid-1,R,AccNo)
n=int(input("Enter number of books in the library"))
accNo=[]
for i in range(n):
    name=input("Enter name")
    author=input("Enter author")
    date=input("Enter date of purchase")
    accNo.append(int(input("Enter Accession Number")))
    status=input("Enter availability Status of the book")
search=int(input("Enter the accession number to be searched"))
c=bsearch(0,n-1,search,accNo)
if c==-1:
    print("Not Found")
else:
    print("Found")
