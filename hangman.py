import random


def hangman():
    word = random.choice(
        ["batman", "claymore", "sniper", "angel", "cat", "fisherman", "farming", "simulation", "computer",
         "conscience"])
    validLetters = 'abcdefghijklmnoprstuwxyz'
    turns = 10
    guessesMade = ''

    while len(word) > 0:
        main = ""
        missed = 0

        for letter in word:
            if letter in guessesMade:
                main = main + letter
            else:
                main = main + "_" + ""
        if main == word:
            print(main)
            print("You Win!")
            break

        print("Enter a letter: ", main)
        guessP = input()
        guess = guessP.lower()

        if guess in validLetters:
            guessesMade = guessesMade + guess
        else:
            print("Enter a valid character.")
            guess = input()

        if guess not in word:
            turns = turns - 1
            if turns == 9:
                print("9 turns left")
                print("            ")
            if turns == 8:
                print("8 turns left")
                print("      o      ")
            if turns == 7:
                print("7 turns left")
                print("      o      ")
                print("      |      ")
            if turns == 6:
                print("6 turns left")
                print("      o      ")
                print("      |      ")
                print("     /       ")
            if turns == 5:
                print("5 turns left")
                print("      o      ")
                print("      |      ")
                print("     / \     ")
            if turns == 4:
                print("4 turns left")
                print("     \o      ")
                print("      |      ")
                print("     / \     ")
            if turns == 3:
                print("3 turns left")
                print("     \o/     ")
                print("      |      ")
                print("     / \     ")
            if turns == 2:
                print("2 turns left")
                print("     \o/     ")
                print("      |      ")
                print(" ____/ \     ")
            if turns == 1:
                print("1 turn left")
                print("|    \o/     ")
                print("|     |      ")
                print("|____/ \     ")
            if turns == 0:
                print("You lose!")
                print("|-----| ")
                print("|    \o/     ")
                print("|     |      ")
                print("|____/ \     ")


print("Try to guess the word in less than 10 attempts. ")
print("Good luck!")
print("----------------------")
hangman()
print()
