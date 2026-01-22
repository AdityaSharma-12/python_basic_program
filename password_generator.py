import string
import random
n=int(input("Enter password length:"))
char=string.ascii_letters+string.digits+string.punctuation
for i in range(n+1):
    print(random.choice(char),end="")
