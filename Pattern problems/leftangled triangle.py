name='syed'
#left angled traingle row
for i in range(1,6):
    for j in range(5,i,-1):
        print(' ',end='')
    for k in range(0,i):
        print(i,end='')
    print()
#left angled traingle column
for i in range(1,6):
    for j in range(5,i,-1):
        print(' ',end='')
    for k in range(i,0,-1):
        print(k,end='')
    print()
#upper row
for i in range(1,6):
    for j in range(5,i,-1):
        print(' ',end='')
    for k in range(0,i):
        print(chr(64+i),end='')
    print()
#upper column
for i in range(1,6):
    for j in range(5,i,-1):
        print(' ',end='')
    for k in range(i,0,-1):
        print(chr(k+64),end='')
    print()
#lower row
for i in range(1,6):
    for j in range(5,i,-1):
        print(' ',end='')
    for k in range(0,i):
        print(chr(96+i),end='')
    print()
#lower column
for i in range(1,6):
    for j in range(5,i,-1):
        print(' ',end='')
    for k in range(i,0,-1):
        print(chr(k+96),end='')
    print()
#*pattern
for i in range(1,6):
    for j in range(5,i,-1):
        print(' ',end='')
    for k in range(i,0,-1):
        print("*",end='')
    print()
#name pattern column
for i in range(0,len(name)):
    for j in range(5,i,-1):
        print(' ',end='')
    for k in range(i,-1,-1):
        print(name[k],end='')
    print()
#name pattern row
for i in range(0,len(name)):
    for j in range(5,i,-1):
        print(' ',end='')
    for k in range(0,i+1):
        print(name[i],end='')
    print()

#inversed left triangle row
for i in range(5,0,-1):
    for j in range(5-i):
        print(' ',end='')
    for k in range(i):
        print(i,end='')
    print()
#inverted left triangle column
for i in range(5,0,-1):
    for j in range(5-i):
        print(' ',end='')
    for k in range(i,0,-1):
        print(k,end='')
    print()
#inverted upper row
for i in range(5,0,-1):
    for j in range(5-i):
        print(' ',end='')
    for k in range(i):
        print(chr(64+i),end='')
    print()
#inverted upper column
for i in range(5,0,-1):
    for j in range(5-i):
        print(' ',end='')
    for k in range(i,0,-1):
        print(chr(k+64),end='')
    print()
#inverted lower row
for i in range(5,0,-1):
    for j in range(5-i):
        print(' ',end='')
    for k in range(i):
        print(chr(i+96),end='')
    print()
#inverted lower column
for i in range(5,0,-1):
    for j in range(5-i):
        print(' ',end='')
    for k in range(i,0,-1):
        print(chr(k+96),end='')
    print()
#*pattern
for i in range(5,0,-1):
    for j in range(5-i):
        print(' ',end='')
    for k in range(i,0,-1):
        print("*",end='')
    print()
#inverted name pattern row
for i in range(len(name)-1,-1,-1):
    for j in range(len(name)-1-i):
        print(' ',end='')
    for k in range(i+1):
        print(name[i],end='')
    print()
#inverted name pattern column
for i in range(len(name)-1,-1,-1):
    for j in range(len(name)-1-i):
        print(' ',end='')
    for k in range(i,-1,-1):
        print(name[k],end='')
    print()