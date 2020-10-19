import database

#count words count and return in dict format
def count(text):
    cache=''
    res={}
    for ch in text:
        if ch.isalnum():
            cache+=ch
        elif cache !='':
            cache=cache.lower()
            if cache in res.keys():
                res[cache]+=1
            else :
                res[cache]=1
            cache =''
    return res


def getscores(pth):
    scores={}
    with open(pth,'r',encoding='utf-8') as f:
        res=count(f.read())
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
        #print(f'\n"{category}"\t:\t{score}\n')
        scores[category]=score
    return scores