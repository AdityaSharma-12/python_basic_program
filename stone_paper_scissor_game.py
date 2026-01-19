import random
c=['stone','paper','scissor']
r=0
while True:
    comp=random.choice(c)
    a=input("Enter your response(stone,paper,scissor):").lower()
    if a not in c:
        print("Invalid input,try again")
        continue
    r+=1
    if a==comp:
        print("Tie,retry")
    elif a=='stone' and comp=='paper':
        print ("paper holds rock.computer wins,retry")
    elif a=='paper' and comp=='scissor':
        print ("scissor cuts paper.computer wins,retry")
    elif a=='scissor' and comp=='stone':
        print ("stone breaks scissor.computer wins,retry")
    else:
        print("You win")
        break
print(f"you take {r} turns to win")




