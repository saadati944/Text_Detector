import database, process, funcs
import sys, os


if sys.argv[0]==__file__:
    sys.argv.pop(0)

def execargs():
    if sys.argv[0]=='-h' or sys.argv[0]=='--help' or sys.argv[0]=='/?':
        funcs.help()
    elif sys.argv[0]=='-c':
        database.load()
        for k in database.database.keys():
            print(k)
    elif sys.argv[0]=='-w':
        if not funcs.areUsure():
            print ('failed')
        database.database={}
        database.dump()
        print('\nok\n')
    elif sys.argv[0]=='-a' and len(sys.argv)==3 and os.path.exists(sys.argv[2]):
        database.load()
        with open(sys.argv[2] ,'r' ,encoding='utf-8') as f:
            database.addCountedWords(process.count(f.read()),sys.argv[1])
        database.dump()
        print('\nok\n')
    elif sys.argv[0]=='-p' and len(sys.argv)==2 and os.path.exists(sys.argv[1]):
        database.load()
        scores=process.getscores(sys.argv[1])
        for cat in scores.keys():
            print(f'{cat}\t:\t{scores[cat]}')

    

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

if len(sys.argv)!=0:
    execargs()
elif __name__=='__main__':
    main()