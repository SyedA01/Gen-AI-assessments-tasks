#1.Write a program to remove lowercase substrings from a given string.

def removelow():
    s=input('Enter a string:')
    out=''
    for i in s:
        if not i.islower():
            out+=i
    print(out)

removelow()

#2.Write a program that reads a given expression and evaluates it
def evalexp():
    s=input('Enter a expression: ')
    print(eval(s))

evalexp()

#3.Write a program to insert spaces between words starting with capital letters.

def insert_space():
        sentence=input("Enter the words")
        out=[]
        current=sentence[0]

        for i in sentence[1:]:
            if i.isupper():
                out.append(current)
                current=i
            else:
                current+=i
        out.append(current)
        print(' '.join(out))

insert_space()

     