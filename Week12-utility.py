#https://github.com/snegrete1101/CSCI-102-wk12-utilities.git
#Sebastian Negrete-Alamillo
#CSCI 102 - Section E
#Week 12 - Part B

def PrintOutput(string):
    print('OUTPUT ', string)

def LoadFile(path):
    with open('test.txt', 'r') as path:
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
