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
