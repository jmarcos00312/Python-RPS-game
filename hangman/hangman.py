import random
from turtle import pos
# importing the words from another file as a module
import words
# importing the stages from another file as a module
import hangman_art


# choosing a random word
choosenWord = random.choice(words.word_list)
# initializing players lives
lives = 6
# empty string to display to user
display = []
# descision if the game is over
end_of_game = False
# switching each letter of the choosen word to blank and adding it to display list
for _ in choosenWord:
    display += "_"
    
    # while the end of game is False
while not end_of_game:
    print(choosenWord)
    print(display)
    # asking the user for a letter to guess
    userguess = input("Enter a letter: ")
    # for each index of the length of the choosen word
    for position in range(len(choosenWord)):
        # getting the letter of the current index
        letter = choosenWord[position]
        # if the current letter and the userGuess is the same
        if userguess == letter:
            # instead of showing a blank, show the letter instead
            display[position] = letter
# ==============================
# out of the for loop
# ==============================
    # but if the userGuess is not in the choosenWord
    if userguess not in choosenWord:
        # take away lives from the user
        lives -= 1
        # if the users lives is equal to 0
        if lives == 0:
            # switch end of game to True
            end_of_game = True
            # and letting the user know that they lose
            print("You lose.")
    
    # but if there is no more blank in the display (all the letter is guessed)
    if "_" not in display:
        # switch end of game to True
        end_of_game = True
        # end let the user know that they win
        print("You win.")
    
    
# showing how many lives the user still have
    print(hangman_art.stages[lives])
