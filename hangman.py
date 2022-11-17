import os
import random
import math

os.system('clear')

global mainWordArr
mainWordArr = ['apple', 'banana', 'coconut', 'dolphin', 'elephant', 'fish']

def fillWordGenerate():
    global word
    global fillWord
    word = []
    fillWord = []

    for items in random.choice(mainWordArr):
        fillWord.append(items)
        word.append(items)

    randVal = random.sample(range(0, len(fillWord)),
                            math.floor(len(fillWord) / 2))
    for items in randVal:
        fillWord[items] = "_"

    print("Fill this word ", fillWord)
    print("\n")


guesses = 0
def hangMan():
    global guesses
    global value
    value = input("Enter your guess :- ")

    for i, items in enumerate(fillWord):
        if items == "_":
            if value == word[i]:
                fillWord[i] = value
                print(fillWord)
            elif value != word[i]:
                guesses += 1
                print("not matched!!!")
            break

    if guesses == 0:
        print("________      ")
        print("|      |      ")
        print("|             ")
        print("|             ")
        print("|             ")
        print("|             ")
    elif guesses == 1:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|             ")
        print("|             ")
        print("|             ")
    elif guesses == 2:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /       ")
        print("|             ")
        print("|             ")
    elif guesses == 3:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|      ")
        print("|             ")
        print("|             ")
    elif guesses == 4:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|\     ")
        print("|             ")
        print("|             ")
    elif guesses == 5:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|\     ")
        print("|     /       ")
        print("|             ")
    elif guesses == 6:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|\     ")
        print("|     / \     ")
        print("|             ")      
    elif guesses > 6:
        print("You lose!!!")      
        playAgainInp = input("Wanna play again?...y for yes other keys for no :- ")
        if playAgainInp == "y":
            guesses = 0
            os.system("clear")
            print("\n")
            fillWordGenerate()
            hangMan()


    if "_" in fillWord:
        hangMan()
    elif "_" not in fillWord:
        print("You won!!!")      
        playAgainInp = input("Wanna play again?...y for yes other keys for no :- ")
        if playAgainInp == "y":
            guesses = 0
            os.system("clear")
            fillWordGenerate()
            hangMan()

fillWordGenerate()
hangMan()
