import random

words = ["python","developer","hangman","computer","programming"]

word = random.choice(words)
guessed_letters = []
tries = 6

print("welcome to hangman!")

while tries > 0:
    display_word =""
    
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "

        else:
            display_word += "_ "

    print("\n Word:",display_word.strip())
    print("Tries left:", tries)

    if "_" not in display_word:
        print("You won!")
        break

    guess = input("enter a letter").lower()

    if guess in guessed_letters:
        print("already guessed!")
        continue

    guessed_letters.append(guess)

    if guess not in word:
        tries -= 1
        print("Wrong guess")

else:
    print("You lost! The word was:",word)