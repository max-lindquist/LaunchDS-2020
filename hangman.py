import random

## Creating a list of possible words that can be chosen
list_of_words = ["words", "hangman", "fun"]

## The user determines how many guesses they want to have
print("Let's play Hangman!!\n")
guesses = int(input("How many guesses do you want? \n"))

## The word to guess is picked from the list and a list is created to represent the word
wordToGuess = random.choice(list_of_words)
letterList = []
for letter in wordToGuess:
    letterList.append('_')

print(letterList)

guessedLetters = []

while guesses > 0:
    wrong = True
    index = 0

    guess = input("Guess a character: ")

    for letter in wordToGuess:
        if letter == guess or letter == guess.lower():
            letterList.insert(index, guess.lower())
            letterList.pop(index + 1)
            wrong = False
        index += 1
    if wrong:
        guesses -= 1

    print(letterList)

    if "_" not in letterList:
        print("You win!!!")
        break


if guesses == 0:
    print("\nYou lose!!")