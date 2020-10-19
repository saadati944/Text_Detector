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
    print(' e\t:\texit')                                #v
    print(' p\t:\tprocess new text file')               #v
    print(' a\t:\tadd new file to database')            #v
    print(' d\t:\tdump database')                       #v
    print(' l\t:\tload database (ignore changes)')      #v
    print(' w\t:\twipe database')                       #v
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
        elif ans=='w':
            rnd=random.random()
            if input(f"enter '{rnd}' to continue : ")!=str(rnd):
                print('not equal !!!')
                input('press enter to continue ...')
                continue
            database.database={}
            database.dump()
            input('ok\npress enter to continue ...')
        elif ans=='p':
            pth=input('enter file name : ')
            # res means words count of given file
            with open(pth,'r',encoding='utf-8') as f:
                res=process.count(f.read())
            restotal=0.0
            for k in res:
                restotal+=res[k]
            for category in database.database.keys():
                score=0.0
                cat=database.database[category]
                cattotal=0.0
                for k in cat:
                    cattotal+=cat[k]
                for k in res :
                    if k in cat:
                        score+=1-abs((cat[k]/cattotal)-(res[k]/restotal))
                #show resaults
                print(f'\n"{category}"\t:\t{score}\n')
            input('\npress enter to continue ...')


if __name__=='__main__':
    main()