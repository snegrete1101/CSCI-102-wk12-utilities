#https://github.com/snegrete1101/CSCI-102-wk12-utilities.git
#Sebastian Negrete-Alamillo
#CSCI 102 - Section E
#Week 12 - Part B

def PrintOutput(string):
    print('OUTPUT ', string)

def LoadFile(path):
    with open(path, 'r') as path:
        a = path.readlines()
        out =[]
        for i in a:
            b = i.strip()
            out.append(b)
        return out

def UpdateString(string, char, index):
    a = [i for i in string]
    a[index] = char
    out = ''.join(a)
    PrintOutput(out)

def FindWordCount(list,word):
    words = ''.join(list)
    out = words.count(word)
    return out

def ScoreFinder(players, scores, name):
    name_low = name.lower()
    name_out = name_low.capitalize()
    a = ' '.join(players)
    low = a.lower()
    ls_low = low.split()
    if name_low in ls_low:
        location = ls_low.index(name_low)
        score = scores[location]
        print("OUTPUT %s got a score of %d" % (name_out,score))
    else:
        print("OUTPUT player not found")

def Union(list_a, list_b):
    out = []
    for i in list_a:
        if i not in out:
            out.append(i)
    for j in list_b:
        if j not in out:
            out.append(j)
    return out

def Intersection(list_a, list_b):
    out = []
    for i in list_a:
        if i in list_b:
            out.append(i)
    return out

def NotIn(list_a, list_b):
    out = []
    for i in list_a:
        if i not in list_b:
            out.append(i)
    return out
