import json
import os

database={}

defaultDatabasePath='data'

def load():
    if os.path.exists(defaultDatabasePath):
        with open(defaultDatabasePath ,'r' ,encoding='utf-8') as f:
            database=json.loads(f.read())

def dump():
    with open(defaultDatabasePath ,'w' ,encoding='utf-8') as f:
        f.write(json.dumps(database))


def addCountedWords(resault,category):
    global database
    if not (category in database):
        database[category]=resault
        return
    for k in resault.keys():
        if k in database[category]:
            database[category][k]+=resault[k]
        else :
            database[category][k]=resault[k]