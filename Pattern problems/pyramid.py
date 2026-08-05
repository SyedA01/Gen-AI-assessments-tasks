name='syed'
#pyramid row
for i in range(1,6):
    for j in range(5,i,-1):
        print(' ',end='')
    for k in range(0,i):
        print(i,end=' ')
    print()
#pyramid column
for i in range(1,6):
    for j in range(5,i,-1):
        print(' ',end='')
    for k in range(i,0,-1):
        print(k,end=' ')
    print()
#pyramid uppercase row
for i in range(1,6):
    for j in range(5,i,-1):
        print(' ',end='')
    for k in range(0,i):
        print(chr(64+i),end=' ')
    print()
#pyramid uppercase column
for i in range(1,6):
    for j in range(5,i,-1):
        print(' ',end='')
    for k in range(i,0,-1):
        print(chr(k+64),end=' ')
    print()
#pyramid lowercase row
for i in range(1,6):
    for j in range(5,i,-1):
        print(' ',end='')
    for k in range(0,i):
        print(chr(96+i),end=' ')
    print()
#pyramid lowercase column
for i in range(1,6):
    for j in range(5,i,-1):
        print(' ',end='')
    for k in range(i,0,-1):
        print(chr(k+96),end=' ')
    print()
#pyramid *pattern
for i in range(1,6):
    for j in range(5,i,-1):
        print(' ',end='')
    for k in range(i,0,-1):
        print("*",end=' ')
    print()
#pyramid name pattern row
for i in range(0,len(name)):
    for j in range(5,i,-1):
        print(' ',end='')
    for k in range(i,-1,-1):
        print(name[k],end='')
    print()
#pyramid name pattern column
for i in range(0,len(name)):
    for j in range(5,i,-1):
        print(' ',end='')
    for k in range(0,i+1):
        print(name[i],end='')
    print()



#inversed pyramid row
for i in range(5,0,-1):
    for j in range(5-i):
        print(' ',end='')
    for k in range(i):
        print(i,end=' ')
    print()
#inverted pyramid column
for i in range(5,0,-1):
    for j in range(5-i):
        print(' ',end='')
    for k in range(i,0,-1):
        print(k,end=' ')
    print()
#inverted pyramid upper row
for i in range(5,0,-1):
    for j in range(5-i):
        print(' ',end='')
    for k in range(i):
        print(chr(64+i),end=' ')
    print()
#inverted pyramid upper column
for i in range(5,0,-1):
    for j in range(5-i):
        print(' ',end='')
    for k in range(i,0,-1):
        print(chr(k+64),end=' ')
    print()
#inverted pyramid lower row
for i in range(5,0,-1):
    for j in range(5-i):
        print(' ',end='')
    for k in range(i):
        print(chr(i+96),end=' ')
    print()
#inverted pyramid lower column
for i in range(5,0,-1):
    for j in range(5-i):
        print(' ',end='')
    for k in range(i,0,-1):
        print(chr(k+96),end=' ')
    print()
#*pattern
for i in range(5,0,-1):
    for j in range(5-i):
        print(' ',end='')
    for k in range(i,0,-1):
        print("*",end=' ')
    print()
#inverted name pyramid pattern row
for i in range(len(name)-1,-1,-1):
    for j in range(len(name)-1-i):
        print(' ',end='')
    for k in range(i+1):
        print(name[i],end=' ')
    print()
#inverted name pyramid  pattern column
for i in range(len(name)-1,-1,-1):
    for j in range(len(name)-1-i):
        print(' ',end='')
    for k in range(i,-1,-1):
        print(name[k],end=' ')
    print()