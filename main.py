from os import system,name
import database


#clear screen
def clear():
    _= system('cls' if name=='nt' else 'clear')

#show menu
def menu():
    print('text detector version 0.0')
    print()
    print(' e\t:\texit')
    print(' p\t:\tprocess new text file')
    print(' a\t:\tadd new file to database')
    print(' d\t:\tdump database')
    print(' l\t:\tload database (ignore changes)')
    print(' w\t:\twipe database')
    print()


def main():
    database.load()
    while True:
        clear()
        menu()
        ans=input('your choice : ')
        if ans=='e':
            exit()

if __name__=='__main__':
    main()