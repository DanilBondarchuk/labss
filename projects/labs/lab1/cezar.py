def cezar(info):
    voc = "ABCDEFGIHJKLMNOPQRSTUVWXYZABCDEFGIHJKLMNOPQRSTUVWXYZabcdefgihjklmnopqrstuvwxyzabcdefgihjklmnopqrstuvwxyz1234578901234567890/ / "
    key = 1
    s = str(info)
    r = ""
    for i in s:
        place = voc.find(i)
        nplace = place + key
        if i in voc:        
           r += voc[nplace]
        else:
           r += voc    
    return r

def decezar(info):
    voc = "ABCDEFGIHJKLMNOPQRSTUVWXYZABCDEFGIHJKLMNOPQRSTUVWXYZabcdefgihjklmnopqrstuvwxyzabcdefgihjklmnopqrstuvwxyz1234578901234567890/ / "
    key = 1
    s = str(info)
    r = ""
    for i in s:
        place = voc.find(i)
        nplace = place - key
        if i in voc:        
           r += voc[nplace]
        else:
           r += voc    
    return r
