# author: Tanishq Patil
# date: October 5, 2022
# file: test_hangman.py tests a hangman.py
# input: file 'dictionary_short.txt'
# output: possible assertion errors

import hangman
import sys
import io


if __name__ == '__main__':
    
    # test import_dictionary(filename)
    dict_standard = {2:['ad'],
                     3:['bat'],
                     4:['card'],
                     5:['dress'],
                     6:['engine'],
                     7:['T-shirt'],
                     8:['gasoline'],
                     9:['gathering'],
                     10:['evaluation'],
                     11:['self-esteem'],
                     12:['unemployment']}
    file = 'C:\\Users\\tqpat\\OneDrive\\Documents\\Python\\dictionary-short.txt'
    dictionary = hangman.import_dictionary(file)
    assert dictionary == dict_standard

    # test get_game_options()
    
    output_standard = '\nThe word size is set to 4.\n\nYou have 4 lives.\n'
    hangman.input = lambda x:'4' # redirect input
    stdout = sys.stdout
    sys.stdout = io.StringIO()   # redirect stdout
    size, lives = hangman.get_game_options()
    output = sys.stdout.getvalue()
    sys.stdout = stdout          # restore stdout
    assert size == 4
    assert lives == 4
    assert output == output_standard
    #test spaceOut()
    output_standard="O O O O"
    stdout=sys.stdout
    sys.stdout=io.StringIO()
    out=hangman.spaceOut("OOOO", 1)
    sys.stdout=stdout
    assert out==output_standard
    #test getPlayAgain()
    output_standard = "n"
    stdout=sys.stdout
    sys.stdout=io.StringIO()
    hangman.input = lambda x:'n'
    z=hangman.getPlayAgain()
    sys.stdout=stdout
    assert z== output_standard
    #test getLetter()
    hangman.letterChosen=[]
    output_standard="\nPlease choose a new letter >"
    stdout=sys.stdout
    sys.stdout=io.StringIO()
    hangman.input = lambda y:'a'
    y=hangman.getLetter()
    out=sys.stdout.getvalue()
    sys.stdout=stdout
    assert y=='a'
    #test wordDisplay(hyPos,word)
    output_standard="_-_____"
    stdout=sys.stdout
    sys.stdout=io.StringIO()
    out=hangman.wordDisplay([], "t-shirt")
    sys.stdout=stdout
    assert out==output_standard
    

    print('Everything looks good! No assertion errors!')