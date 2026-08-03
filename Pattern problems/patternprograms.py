#i-->outer loop--->row printing--->tells which number to print
#j-->inner loop--->column printing--->tells howmany times to print

#row wise printing
'''for i in range(0,6):
    for j in range(0,i):
        print(i,end=" ")
    print()'''

#columnwise printing
'''for i in range(0,6):
    for j in range(0,i):
        print(j,end=" ")
    print()'''

#*pattern
'''for i in range(0,6):
    for j in range(0,i):
        print("*",end=" ")
    print()'''

#rowwise-upperalphabet printing
'''for i in range(1,6):
    for j in range(0,i):
        print(chr(i+64),end=" ")
    print()'''

#columnwise-upperalphabet printing
'''for i in range(1,6):
    for j in range(0,i):
        print(chr(j+64),end=" ")
    print()'''

#rowwise-loweralphabet printing
'''for i in range(1,6):
    for j in range(0,i):
        print(chr(i+96),end=" ")
    print()'''

#columnwise-loweralphabet printing
'''for i in range(1,6):
    for j in range(0,i):
        print(chr(j+97),end=" ")
    print()'''
#inverse row-wise right angled triangle
'''for i in range(5,0,-1):
    for j in range(0,i):
        print(i,end=" ")
    print()'''

#inverse column-wise right angled triangle
'''for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()'''

#inverse column-wise *pattern right angled triangle
'''for i in range(5,0,-1):
    for j in range(i,0,-1):
        print("*",end=" ")
    print()'''

#inverse column-wise upper-alphabet right angled triangle
'''for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(chr(j+64),end=" ")
    print()'''

#inverse column-wise lower-alphabet right angled triangle
'''for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(chr(j+96),end=" ")
    print()'''

#inverse row-wise upper-alphabet right angled triangle
for i in range(5,0,-1):
    for j in range(i):
        print(chr(i+64),end=" ")
    print()

#inverse row-wise lower-alphabet right angled triangle
for i in range(5,0,-1):
    for j in range(i):
        print(chr(i+96),end=" ")
    print()





