import random as rnd
from words import words
from hung_up_man import hung_up_man
import string as str
import os




def validate_word(words):
    word = rnd.choice(words)

    while (' ' in word) or ('-' in word):
        word = rnd.choice(words)
        #print(word)
    
    return word


def hangman(word):
        #alphabet from A to Z
        alphabet = set(str.ascii_lowercase)
        #separating the word letter by letter
        word_letters = set(word.lower())
        #new set for used letters to store
        used_letters = set()
        #amount of allowed tries
        tries = 6
        #guess = ' '
        print(word_letters)
        
        
        while len(word_letters)>0 and tries>0:
            #set to store guessed letters
            #newlist = [expression for item in iterable if condition == True]
            print(hung_up_man[tries])
            print(f"you have already used the following leters: " , ", ".join(used_letters), "\n")
            
            ##########################################################################
            #this line is the for loop from bellow summarized in one line
            letter_list = ['-' if x in word_letters else x for x in word]
            
           # for x in word:
            #    if x in word_letters:
             #       letter_list.append('-')
              #  elif x not in word_letters:
               #     letter_list.append(x)
            #will concatenate the list so it can be printed
            print("current word: ", " ".join(letter_list))
            ############################################################################

            
            #################################################################################
            #this line of code will validate the input, will make sure its valid and the string lenght is not higher than 1
            guess = input("please, provide a letter to guess the word: \n").lower()
            while len(guess)>1:
                guess = input("please, provide only one letter, only one: \n").lower()
            
            while guess not in alphabet:
                guess = input("please, introduce a valid character in the alphabet: \n").lower()
            ##################################################################################


            ##################################################################################
            #will validate if the guess is right or wrong
            if guess in word_letters:
                #will remove from the set since the character is already guessed
                word_letters.remove(guess)
                #will add to the used letters, just so the user can keep track of the already used letters
                used_letters.add(guess)
                print(f"NICE!, {len(word_letters)} letters to go!")
            elif guess not in word_letters:
                #will add to the used letters, just so the user can keep track of the already used letters
                used_letters.add(guess)
                #print("keep trying!")
                tries -= 1
            #os.system("cls")
            ##################################################################################

        
        #controlls the winning or losing message
        print(hung_up_man[tries])
        if len(word_letters)>0:
            print("YOU LOST HA HA!")
            print(f"the word was: {word}")
        elif len(word_letters)<=0:
            print("YOU WON YEAAAAAHHH")
            print(f"the word was: {word}")




word = validate_word(words)
print(word)
hangman(word)






    



