a=int(input("Enter number:"))
d=a
num=0
while a>0:
    b=a%10
    num*=10
    num+=b
    a=a//10
print(f"Reverse of provided number {d} is {num}" )
if d==num:
    print("Pallindrome")
else:
    print("Not pallindrome")




