import database, process, funcs
import sys, os



changes=''


def main():
    global changes
    database.load()
    while True:
        funcs.clear()
        funcs.menu()
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
            if not funcs.areUsure():
                input('press enter to continue ...')
                continue
            database.dump()
            input('ok\npress enter to continue ...')
        elif ans=='l':
            if changes=='':
                input('no changes detected !!!\npress enter to continue ...')
                continue
            if not funcs.areUsure():
                input('press enter to continue ...')
                continue
            database.load()
            input('ok\npress enter to continue ...')
        elif ans=='w':
            if not funcs.areUsure():
                input('press enter to continue ...')
                continue
            database.database={}
            database.dump()
            input('ok\npress enter to continue ...')
        elif ans=='p':
            pth=input('enter file name : ')
            scores=process.getscores(pth)
            print()
            for cat in scores.keys():
                print(f'{cat}\t:\t{scores[cat]}')
            print()
            input('\npress enter to continue ...')

if __name__=='__main__':
    main()