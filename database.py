import json

database={}

defaultDatabasePath='data'

def load():
    with open('defaultDatabasePath' ,'r' ,encoding='utf-8') as f:
        database=json.loads(f.read())

def dump():
    with open('defaultDatabasePath' ,'w' ,encoding='utf-8') as f:
        f.write(json.dumps(database))