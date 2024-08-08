# How to play hangman game
# first is the game intro
print("Welcome to the hangman game")
print("How to play : \n 1) A random word will be generated \n 2) You will have to guess the word \n 3) There will be 7 chances to guess the word, if you fail this guy will die \n\t  O""\n\t /|\\ \n\t / \\ ")
print("Let's play !!!!")

# set that will make sure only alphabets are entered
validentry = set("qwertyuioplkjhgfdsazxcvbnm")

# importing random for generating random words
import random
from Words import Word_list     # importing Word_list form the file Words that has a collection of letters
w = random.choice(Word_list)    # w is the chosen word
w = w.lower()                         
l = len(w)

def play():
    
    tries = 9
    guess_made = ''
    while l>0:      # loop will operate according to the length of the word
        main_w = ''

        for letter in w : # loop will carry out the main function of the program that is generating '_' according to the length and replacing those '_' with words guessed by the user
            if letter in guess_made:
                main_w = main_w + letter
            else:
                main_w = main_w + "_ "
 
            if main_w == w:
                print(main_w)
                print("You won !!!")
                break
        
        print("Guess the word", main_w)
        guess = input()
           
        if guess in validentry:  # this checks if the entry made is valid or no
            guess_made = guess_made + guess
        else :
            print("Enter valid characters")
            guess = input()

        if guess not in w :   # this conditional statement makes the hangman and works with number of tries left
            tries = tries - 1

            if tries == 8:
                print("8 turns left")
                print("----------------------------")
            if tries == 7:
                print("7 turns left")
                print("----------------------------")
                print("              |             ")
            if tries == 6:
                print("6 turns left")
                print("----------------------------")
                print("              |             ")
                print("              O             ")
            if tries == 5:
                print("5 turns left")
                print("----------------------------")
                print("              |             ")
                print("              O             ")
                print("              |             ")
            if tries == 4:
                print("----------------------------")
                print("              |             ")
                print("              O             ")
                print("             /|             ")
            if tries == 3:
                print("3 turns left")
                print("----------------------------")
                print("              |             ")
                print("              O             ")
                print("             /|\\           ")
            if tries == 2:
                print("2 turns left")
                print("----------------------------")
                print("              |             ")
                print("              O             ")
                print("             /|\\           ")
                print("             /              ")
            if tries == 1:
                print("1 turns left")
                print("----------------------------")
                print("              |             ")
                print("              O             ")
                print("             /|\\           ")
                print("             / \\           ")
            if tries == 0:
                print("You failed to guess the word... An innocent man died !!!! The word was : ",w)

play()
