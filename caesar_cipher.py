import string
alpha=list(string.ascii_letters+string.digits+string.punctuation+string.whitespace)
def encryption(text,keys):
    cipher_text=""
    for i in text:
        position=alpha.index(i)
        new_position=(position+keys)%len(alpha)
        cipher_text+=alpha[new_position]
    print(f"Your encrypted message is:{cipher_text}")
def decryption(text,keys):
    cipher_text=""
    for i in text:
        position=alpha.index(i)
        new_position=(position-keys)%len(alpha)
        cipher_text+=alpha[new_position]
    print(f"Your decrypted message is:{cipher_text}")
print(alpha)
while True:
    what_to_do=input("Type encrypt for encryption or decrypt for decryption:").lower()
    text=input("Type your message:")
    keys=int(input("Enter no of shift keys:"))
    if what_to_do == "encrypt":
        encryption(text,keys)
        a=input("You want to play again(Y/N):").lower()
        if a=='n':
            print("Thank you,Bye")
            break  
    elif what_to_do == "decrypt":
        decryption(text,keys)
        a=input("You want to play again(Y/N):").lower()
        if a=='n':
            print("Thank you,Bye")
            break   
    else:
        print("Not specified you want to encrypt or decrypt your message")
        

