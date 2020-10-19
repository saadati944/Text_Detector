from os import system,name
import database, process
import random

changes=''


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
    global changes
    database.load()
    while True:
        clear()
        menu()
        ans=input('your choice : ')
        if ans=='e':
            exit()
        elif ans=='a':
            pth=input('enter file name to add to database : ')
            with open(pth,'r',encoding='utf-8') as f:
                cat=input('category name : ')
                database.addCountedWords(process.count(f.read()),cat)
                changes+=f'Add {pth} to database[{cat}].\n'
                input('new file added successfully\npress enter to continue ...')
        elif ans =='d':
            rnd=random.random()
            if input(f"enter '{rnd}' to continue : ")!=str(rnd):
                print('not equal !!!')
                input('press enter to continue ...')
                continue
            database.dump()
            input('ok\npress enter to continue ...')
        elif ans=='l':
            if changes=='':
                input('no changes detected !!!\npress enter to continue ...')
                continue
            rnd=random.random()
            if input(f"enter '{rnd}' to continue : ")!=str(rnd):
                print('not equal !!!')
                input('press enter to continue ...')
                continue
            database.load()
            input('ok\npress enter to continue ...')

if __name__=='__main__':
    main()