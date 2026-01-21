a=int(input("Enter a number:"))
for i in range(a+1):
    b=len(str(i))
    c=i
    s=0
    while c>0:
        l=c%10
        s+=l**b
        c=c//10
    if i==s:
        print (i,end=" ")