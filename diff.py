# Miller - Myers algorithm
# python realization
#
# Nickolay Yegorov


__author__ = "Yegorov Nickolay"

#simple diff for two lists

def simpleDiff(s1, s2):
    l1 = len(s1)
    l2 = len(s2)
    table = []
    table.append(range(0, l1 + 1))
    for i in xrange(1, l2 + 1):
        table.append([0] * (l1 + 1))
    # first pass
    for i in xrange(1, l2 + 1):
        table[i][0] = table[i-1][0] + 1;
        for j in xrange(1, l1 + 1):
            table[i][j] = min(table[i-1][j] + 1, table[i][j-1] + 1, table[i-1][j-1]);
            if s1[j-1] == s2[i-1] :
                table[i][j] = min(table[i][j],table[i-1][j-1])
    # back track
    j, i = l1, l2
    result = []
    while (j, i) != (0, 0):
        if j == 0:
            result.append(("+", s2[i-1]))
            i -= 1
        elif i == 0:
            result.append(("-", s1[j-1]))
            j -= 1
        else:
            diag = table[i-1][j-1] 
            up   = table[i-1][j] + 1
            left = table[i][j-1] + 1
            curr = table[i][j]
            if curr == diag and s1[j-1] == s2[i-1]:
                #if s1[j-1] == s2[i-1]:
                result.append((" ", s1[j-1]))
                #else:
                #    result.append(("m", [s1[j-1],s2[i-1]]))
                i -= 1
                j -= 1
            elif curr == left: # -
                result.append(("-", s1[j-1]))
                j -= 1
            else: # curr == up # +
                result.append(("+", s2[i-1]))
                i -= 1
    result.reverse()


def countDiffLastRow(s1,s2):
    l1 = len(s1)
    l2 = len(s2)
    row = range(0,l1+1)
    for j in xrange(1,l2+1):
        rw = [0]*(l1+1)
        rw[0]=j;
        for i in xrange(1,l1+1):
            rw[i] = min(rw[i-1] + 1, row[i] + 1) #+ (0 if s1[i-1] == s2[j-1] else 1))
            if s1[i-1] == s2[j-1]:
                rw[i] = min(rw[i], row[i-1])
        row,rw = rw,row
    return row

def even(number):
    return False if number %2 == 1 else True

def millerMyersDiff(s1,s2):
    if (len(s1)<3) or (len(s2)<3) :
        return simpleDiff(s1, s2)
    l1 = len(s1)
    l2 = len(s2)
    ind = l2/2 if even(l2) else l2/2+1
    row1 = countDiffLastRow(s1, s2[:ind])
    st1 = s1[:]
    st1.reverse()
    st2 = s2[(l2-ind+1):]
    st2.reverse()
    row2 = countDiffLastRow(st1,st2)
    row2.reverse()
    index=0;
    for i in xrange(1,l1+1):
        if row1[index]+row2[index] > row1[i]+row2[i]:
            index = i
    return millerMyersDiff(s1[:index], s2[:ind]) + millerMyersDiff(s1[index:], s2[ind:])

def readFile(path):
    result=[]
    fl = open(path)
    for s in fl:
        result.append(s if s[-1] != '\n' else s[:-1])
    return result


paths = ["file3.txt","file4.txt"]
paths[0]=raw_input()
paths[1]=raw_input()
strs1 = readFile(paths[0])
strs2 = readFile(paths[1])
diff  = millerMyersDiff(strs1, strs2)
for p in diff:
    print p[0], p[1]