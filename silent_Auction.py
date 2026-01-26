lst={}
def highestbider(lst):
    name=max(lst,key=lst.get)
    bid=lst[name]
    return name,bid
while True:
    a=input("Enter your name:")
    b=int(input("Enter your bid:"))
    lst[a]=b
    c=input("Enter is there any other bider(Y/N):").lower()
    if c=="n":
        break
    elif c=="y":
        continue
    else:
        print("You entered wrong i/p")
name,bid=highestbider(lst)
print(f"Here is all the biders:{lst}")
print(f"The winner is {name} with a bid price of {bid}")