from random_word import RandomWords
a=RandomWords()
word=a.get_random_word()
word=word.lower()
letters=list(word)
stages = [
    """
      ------
      |    |
      O    |
           |
           |
           |
    """,
    """
      ------
      |    |
      O    |
      |    |
           |
           |
    """,
    """
      ------
      |    |
      O    |
     /|    |
           |
           |
    """,
    """
      ------
      |    |
      O    |
     /|\   |
           |
           |
    """,
    """
      ------
      |    |
      O    |
     /|\   |
     /     |
           |
    """,
    """
      ------
      |    |
      O    |
     /|\   |
     / \   |
           |
    """
]
g=0
guessed=["_"]*len(word)
lives=6
print("Welcome to hangman game")
print(f"You have {lives} lives and length of word is {len(word)}")
print("Word:"," ".join(guessed))
while lives>0 and "_" in guessed:
    a=input("Enter letter:").lower()
    if a in letters:
        for i in range(len(word)):
            if word[i]==a:
                guessed[i]=a
        print("You guessed correct letter")
    else:
        lives-=1
        p=stages[g]
        print(p)
        print("Wrong guess")
        print(f"Lives left:{lives}")
        g+=1
    print("Word:", " ".join(guessed))
if "_" not in guessed:
    print("Congratulations! You won!")
else:
    print(f"Game Over! The word was: {word}")

        