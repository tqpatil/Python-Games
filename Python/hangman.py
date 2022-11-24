# assignment: programming assignment 1
# author: Tanishq Patil
# date: 10/05/22
# file: hangman.py is a program that allows a user to play the classic game
# "hangman" in command line. It first selects a word based on user input for word size
# and lets the user choose how many lives they will have. The program will
# then print out the game line by line until its end, which will ask the user
# if they want to play again. 
# input: User input of both integers and strings. When setting the word size and number of lives, the input should be integers from 3-12 and
# 1-10. If the user chooses the default, word size will be any size, and number of lives will be 5.
# During the game, the user will input letters, one by one, until they either spell out the letter or fail the game.
# output: "Something went wrong" when encountering an exception and game interface output. When the user sets the wrod size and number of lives, the output will repeat their inputs to the user
# to verify them. During the game, the program will repeatedly output the number of letters(denoted by a '_'), the number of lives
# , and the letters that have already been chosen

from random import choice, random

   # make a dictionary.txt in the same folder where hangman.py is located
alphabet= "abcdefghijklmnopqrstuvwxyz"
banned=[""," "]
# write all your functions here

# make a dictionary from a dictionary file ('dictionary.txt', see above)
# dictionary keys are word sizes (1, 2, 3, 4, …, 12), and values are lists of words
# for example, dictionary = { 2 : ['Ms', 'ad'], 3 : ['cat', 'dog', 'sun'] }
# if a word has the size more than 12 letters, put it into the list with the key equal to 12

def import_dictionary (dictionary_file) :
    dictionary = {}
    max_size = 12
    try :
        for i in range(13):
            dictionary[i]=[]
        with open(dictionary_file) as f:
            for line in f:
                word=line.strip()
                if len(word)<12:
                    dictionary[len(word)].append(word)
                    
                elif len(word)>=12:
                    dictionary[12].append(word)
                   
    except Exception :
        print("Failed to create dictionary of proper size")
    del dictionary[0]
    del dictionary[1]     
    return dictionary

# print the dictionary (use only for debugging)
def print_dictionary (dictionary) :
    # max_size = 12
    # for i in range(max_size):
    #     print(str(i)+":")
    #     print(dictionary[i])
    print(dictionary[12])


    
    pass 

# get options size and lives from the user, use try-except statements for wrong input
def get_game_options () :
    try:
        size=int(input("\nPlease choose a size of a word to be guessed [3 - 12, default any size]:"))
        test=size+1
        if size<=12 and size>=3:
            print("\nThe word size is set to "+str(size)+".")
        else:
            raise ValueError()
    except Exception:
        size=100
        print("\nA dictionary word of any size will be chosen.")
    try:
        lives=int(input("Please choose a number of lives [1 - 10, default 5]: "))
        test=lives+1
        if lives<=10 and lives>=1:
            print("\nYou have " +str(lives) +" lives.")
        else:
            raise ValueError()

    except:
        lives=5
        print("\nYou have "+str(lives)+" lives.")




    return (size, lives)
def spaceOut(printer, amount=1):
    pile= ""
    for char in printer:
        pile= pile + char + " "*amount
    return pile.strip()
def getPlayAgain():
    try:
        playAgain= str(input("Would you like to play again [Y/N]?"))
        playAgain=playAgain.lower()
        playagain=playAgain.strip()
        if playAgain not in "yn" or playAgain in banned or len(playAgain)>1:
            while playAgain not in "yn" or playAgain in banned or len(playAgain)>1:
                    playAgain= str(input("Would you like to play again [Y/N]?"))
                    playAgain=playAgain.lower()
                    playAgain=playAgain.strip() 
    except Exception:
        print("Something went wrong")
    return playAgain
def getLetter():
    try:
        letter=str(input("Please choose a new letter >"))
        letter=letter.lower()
        letter=letter.strip()

        if letter not in alphabet or letter in banned or len(letter)>1:
            while letter not in alphabet or letter in banned or len(letter)>1:
                letter=str(input("\nPlease choose a new letter >"))
                letter=letter.lower()
                letter=letter.strip()
        if letter in letterChosen:
            while letter in letterChosen or letter in banned or letter not in alphabet or len(letter)>1:
                print("\nYou have already chosen this letter.")
                letter=str(input("\nPlease choose a new letter >"))
                letter=letter.lower()
                letter=letter.strip()
    except Exception:
        print("Something went wrong.")
    return letter

def wordDisplay(hyPos,word):
    for m in range(len(word)):
        if word[m]=="-":
                hyPos.append(m)
    if 0<len(hyPos)<2:
        return ("_"*hyPos[0])+"-"+"_"*(len(word)-1-hyPos[0])
    else:
        return "_"*len(word)



# MAIN
    

if __name__ == '__main__' :
    file = "C:\\Users\\tqpat\\OneDrive\\Documents\\Python\\dictionary.txt"
    # make a dictionary from a dictionary file
    dictionary = import_dictionary(file)


    # print the dictionary (use only for debugging)
    # print_dictionary(dictionary)    # remove after debugging the dictionary function import_dictionary

    # print a game introduction
    # START MAIN LOOP (OUTER PROGRAM LOOP)
    print("Welcome to the Hangman Game!")
    # set up game options (the word size and number of lives)
    # select a word from a dictionary (according to the game options)
    # use choice() function that selects an item from a list randomly, for example:
    # mylist = ['apple', 'banana', 'orange', 'strawberry']
    # word = choice(mylist)
    playing=True
    while playing:
        won=False
        lost=False
        options=get_game_options()
        if options[0]==100:
            wSize=choice([3,4,5,6,7,8,9,10,11,12])
        else:
            wSize=options[0]
        word=choice(dictionary[wSize])
        while len(word)!=wSize:
            word=choice(dictionary[wSize])
        lives=options[1]
        end=False
        letter=""
        originalLetterChosenDisplay="Letters chosen:"
        letterChosenDisplay="Letters chosen:"
        letterChosen=[]
        hyPos=[]
        lifeDisplay="O"*lives
        originalWord=word
        word=word.lower()
        emptySpace=wordDisplay(hyPos,word)
        
        holder=0

    # START GAME LOOP   (INNER PROGRAM LOOP)
        count=-1
        lostLife=0
        while end==False:            
            v=[]
            count+=1
            if count ==0:
                letterChosenDisplay=originalLetterChosenDisplay
            else:
                strLetterChosen=" "
                for y in range(len(letterChosen)):
                    if y==0:
                        strLetterChosen+=letterChosen[y]
                    else:
                        strLetterChosen+=", "+letterChosen[y]
                letterChosenDisplay= originalLetterChosenDisplay+strLetterChosen.upper()
            print(letterChosenDisplay)
            printer=spaceOut(emptySpace)
            printer=printer.replace("_", "__")
            printer=printer.replace(" ", "  ")
            print(printer+"   lives: "+ str(lives)+ " "+ lifeDisplay)
            if emptySpace[0:wSize*2].replace("  ","")==word.upper():
                copyWord=word.upper()
                print("Congratulations!!! You won! The word is "+ copyWord+"!")
                won=True
                try:
                    playAgain= getPlayAgain()
                    if playAgain=="n":
                        playing=False
                        print("\nGoodbye!")
                        end=True
                        break
                    elif playAgain=="y":
                        end=True
                        break
                    
                    
                except Exception:
                    print("Something went wrong")
                    playAgain= getPlayAgain()
                    if playAgain=="y":
                        end=True
                        break
                    elif playAgain=="n":
                        playing=False
                        print("\nGoodbye!")
                        end=True
                        break
            if lives==0:
                copyWord=word.upper()
                print("You lost! The word is "+ copyWord+ "!")
                lost=True
                try:
                    playAgain=getPlayAgain()
                    if playAgain.lower()=="n":
                        playing=False
                        print("\nGoodbye!")
                        end=True
                        break
                    elif playAgain.lower()=="y":
                        end=True
                        break
                    
                except Exception:
                    print("Something went wrong")
                    playAgain= getPlayAgain()
                    if playAgain.lower()=="y":
                        end=True
                        break
                    elif playAgain.lower()=="n":
                        playing=False
                        print("\nGoodbye!")
                        end=True
                        break    

            try:
                if won==True or lost==True:
                    end=True
                    break
                letter=getLetter()
                if letter in word:
                    print("\nYou guessed right!")
                    letterChosen.append(letter)
                    for k in range(len(word)):
                        if word[k]==letter:
                            v.append(k)
                    for p in range(len(v)):
                        storage=v[p]
                        emptySpace=emptySpace[:storage]+letter.upper()+emptySpace[storage+1:]
                if letter not in word:
                    print("\nYou guessed wrong, you lost one life.")
                    letterChosen.append(letter)
                    lives=lives-1
                    lostLife+=1
                    for t in range(lostLife):
                        lifeDisplay=lifeDisplay[:t] +"X"+lifeDisplay[t+1:]
                    



            except Exception:
                print("Something went wrong.")
                


            


    

   
    
        
        # format and print the game interface:
        # Letters chosen: E, S, P                list of chosen letters
        # __ P P __ E    lives: 4   XOOOO        hidden word and lives

        # ask the user to guess a letter

        # update the list of chosen letters

        # if the letter is correct update the hidden word,
        # else update the number of lives
        # and print interactive messages      

        # END GAME LOOP   (INNER PROGRAM LOOP)

        # check if the user guesses the word correctly or lost all lives,
        # if yes finish the game

    # END MAIN LOOP (OUTER PROGRAM LOOP)

    # ask if the user wants to continue playing, 
    # if yes start a new game, otherwise terminate the program