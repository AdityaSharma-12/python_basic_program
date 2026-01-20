#fibo=0,1,1,2,3
'''n=int(input("Enter range upto:"))
a=0
b=1
lst=[a,b]
if n<1:
    print("Enter number greater than 0")
elif n==1:
    print([a])
else:
    for i in range(2,n):
        c=a+b
        lst.append(c)
        a=b
        b=c
    print(lst)'''
#using recursion
def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1) + fib(n-2)
a=int(input("Enter range upto:"))
if a<1:
    print("Enter number greater than 1")
else:
    for i in range(a):
        print(fib(i),end=" ")







