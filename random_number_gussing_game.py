import random 
a=random.randint(1,10)
chances=0
while True:
    n=int(input("Guess the number between (1-10):"))
    if(a==n):
        chances+=1
        print(f"You guessed the right number in {chances} chances")
        break
    elif (n>a and n<=10):
        print("Go little lower")
        chances+=1
        continue
    elif (n<a and n<=10):
        print("Go little higher")
        chances+=1
        continue
    else:
        print("You guessed the wrong number not between (1-10)")
        chances+=1
        continue

