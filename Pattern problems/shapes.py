heart=[(1,2),(1,3),(1,5),(1,6),(2,1),(2,4),(2,7),(3,7),(4,2),(4,6),(5,3),(5,5),(6,4)]
for i in range(1,9):
    for j in range(1,9):
        if (i,j) in heart:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
square=[(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(1,8),
        (2,1),(3,1),(4,1),(5,1),(6,1),(7,1),(8,1),
        (8,2),(8,3),(8,4),(8,5),(8,6),(8,7),(8,8),
        (2,8),(3,8),(4,8),(5,8),(6,8),(7,8)]
for i in range(1,9):
    for j in range(1,9):
        if (i,j) in square:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()


    
triangle=[(1,4),(2,3),(2,5),(3,2),(3,6),(4,1),(4,2),(4,3),(4,4),(4,5),(4,6),(4,7)]
for i in range(1,5):
    for j in range(1,8):
        if (i,j) in triangle:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
