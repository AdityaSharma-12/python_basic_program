a=input("Enter your name:").lower()
b=input("Enter your partner name:").lower()
s=a+b
c=["t","r","u","e"]
d=["l","o","v","e"]
count1=0
count2=0
for i in c:
    count1+=s.count(i)
for i in d:
    count2+=s.count(i)
love=int(str(count1)+str(count2))
if love<10 or love>90:
    print(f"Your score is {love} and you both are like coke and soda together")
elif  40<=love<=50:
    print(f"Your score is {love} and you are best couple")
else:
    print(f"Your score is {love}")






