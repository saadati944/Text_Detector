from os import system,name
import random

__version__='0.1'

#clear screen
def clear():
    _= system('cls' if name=='nt' else 'clear')

#show menu
def menu():
    print('text detector version',__version__)
    print()
    print(' e\t:\texit')                                #v
    print(' p\t:\tprocess new text file')               #v
    print(' a\t:\tadd new file to database')            #v
    print(' d\t:\tdump database')                       #v
    print(' l\t:\tload database (ignore changes)')      #v
    print(' w\t:\twipe database')                       #v
    print()

def help():
    print('text detector version',__version__)
    print('\nusage : main.py operand [params]')
    print('\noperands:')
    print(' -p FILENAME\t:\tprocess new text file')
    print(' -w\t\t:\twipe database')
    print(' -c\t\t:\tshow avaliable categories')
    print(' -a CATEGORY FILENAME\t:\tadd new file to database\n')

def areUsure():
    rnd=random.random()
    if input(f"enter '{rnd}' to continue : ")!=str(rnd):
        print('not equal !!!')
        return False
    return True