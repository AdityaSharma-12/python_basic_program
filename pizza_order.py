#small pizza=100,medium piza=180,large pizza=230 and add more cheese =50,add extra pepperoni small=30,medium=50,large=70
bill=0
while True:
    a=input("Which size of pizza you want to order(S/M/L):").lower()
    if a=="s":
        bill+=100
        break
    elif a=="m":
        bill+=180
        break
    elif a=="l":
        bill+=230
        break
    else:
        print("Provide(S/M/L) only not other letter or number")
while True:
    b=input("Do you want to add extra pepperoni(Y/N):").lower()
    if b=="y" and a=="s" :
        bill+=30
        break
    elif b=="y" and a=="m" :
        bill+=50
        break
    elif b=="y" and a=="l" :
        bill+=70
        break
    elif b=="n":
        break
    else:
        print("Provide(Y/N) only not other letter or number")
while True:
    c=input("Do you want to add extra cheese(Y/N):").lower()
    if c=="y":
        bill+=50
        break
    elif c=="n":
        break
    else:
        print("Provide(Y/N) only not other letter or number")
print(f"Your bill is {bill}")

    


