'''heart=[(1,2),(1,3),(1,5),(1,6),(2,1),(2,4),(2,7),(3,7),(4,2),(4,6),(5,3),(5,5),(6,4)]
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
    print()'''

def print_shape(shape, rows, cols):

    for i in range(1, rows + 1):
        for j in range(1, cols + 1):

            if (i, j) in shape:
                print("*", end=" ")
            else:
                print(" ", end=" ")

        print()


'''rectangle = []

rows = 4
cols = 8

for i in range(1, rows + 1):
    for j in range(1, cols + 1):
        rectangle.append((i, j))

print_shape(rectangle, rows, cols)

pentagon = []

rows = 5
cols = 9

for i in range(1, rows + 1):

    start = 5 - i
    end = 5 + i

    if i == 5:
        start = 2
        end = 8

    for j in range(start, end + 1):
        pentagon.append((i, j))

print_shape(pentagon, rows, cols)'''


pentagon = [
    (1, 4),
    (2, 3), (2, 5),
    (3, 2), (3, 6),
    (4, 2), (4, 6),
    (5, 2), (5, 6),
    (6, 2), (6, 3), (6, 4), (6, 5), (6, 6)
]


hexagon = [
    (1, 3), (1, 4), (1, 5),
    (2, 2), (2, 6),
    (3, 1), (3, 7),
    (4, 2), (4, 6),
    (5, 3), (5, 4), (5, 5)
]
octagon = [
    (1, 3), (1, 4), (1, 5),
    (2, 2), (2, 6),
    (3, 1), (3, 7),
    (4, 1), (4, 7),
    (5, 2), (5, 6),
    (6, 3), (6, 4), (6, 5)
]
heptagon = [
    (1, 5),
    (2, 4), (2, 6),
    (3, 3), (3, 7),
    (4, 2), (4, 8),
    (5, 2), (5, 8),
    (6, 2), (6, 8),
    (7, 3), (7, 7),
    (8, 4), (8, 5), (8, 6)
]

rectangle = [
    (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8),
    (2, 1), (2, 8),
    (3, 1), (3, 8),
    (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8)
]
parallelogram = [
    (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9),
    (2, 3), (2, 8),
    (3, 2), (3, 7),
    (4, 1), (4, 6),
    (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6)
]
rhombus = [
    (1, 4),
    (2, 3), (2, 5),
    (3, 2), (3, 6),
    (4, 1), (4, 7),
    (5, 2), (5, 6),
    (6, 3), (6, 5),
    (7, 4)
]
trapezium = [
    (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), # Narrow top
    (2, 2), (2, 8),
    (3, 2), (3, 8),
    (4, 1), (4, 9),
    (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9) # Wide base
]



print_shape(pentagon,6,7)
print_shape(hexagon,5,7)
print_shape(octagon,6,7)
print_shape(heptagon,8,9)
print_shape(rectangle,4,8)
print_shape(parallelogram,5,9)
print_shape(rhombus,7,7)
print_shape(trapezium,5,9)
