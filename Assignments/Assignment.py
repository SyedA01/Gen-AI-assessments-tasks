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


#4.write a program to remove paranthesis area in string
#i/p-- 'My programming language is (java) Python'
#o/p-- 'My programming language is  Python'

def remove_paranthesis_part():
        s=input("Enter a sentence: ")
        out=[]
        for i in s.split():
            if not (i.startswith('(') and i.endswith(')')):
                out.append(i)
        print(' '.join(out))
#remove_paranthesis_part()       

#5.Write a program to split a string  with multiple delimiters
#i/p--'My--name--is--syed--Abdul--Qadir',delimiter="--"
#o/p-- ['My', 'name', 'is', 'syed', 'Abdul', 'Qadir']

def custom_split_multi(string, delimiter):
    result = []
    start_idx = 0
    del_len = len(delimiter)
    i = 0
    
    while i <= len(string) - del_len:
        if string[i : i + del_len] == delimiter:
            result.append(string[start_idx:i])
            start_idx = i + del_len
            i += del_len  
        else:
            i += 1
            
    result.append(string[start_idx:])
    return result

text ="My--name--is--syed--Abdul--Qadir"
print(custom_split_multi(text, "--"))

#6.Write a program to find  (adverbs of howbased) and their positions in a given sentence.
#i/p--"It understands very Quickly and clearly"
#o/p--['very','Quikly','Clearly']
def how_adverb():
    s=input("Enter a sentence: ")

    out=[]
    for i in s.split():
        if i=='very' or i=='VERY' or i.endswith('ly') or i.endswith('LY'):
            out.append(i)
    print(out)
        
#how_adverb()

#7.Write a program to split a string at uppercase letters.
#i/p--'aSsyedAabdulKkathir'
#o/p--['a','syed','abdul','kathir']
def split_word_upper():
        sentence=input("Enter the string: ")
        out=[]
        current=""

        for i in sentence:
            if i.isupper():
                out.append(current)
                current=""
            else:
                current+=i
        out.append(current)
        print(out)
#split_word_upper()

          
#8.Write a program to remove everything except alphanumeric characters from a string.
#i/p--'Syed@2001'
#o/p--'Syed2001'
def remove_special_ch():
    s=input('Enter a string: ')
    res=[char for char in s if  char.isalnum()]
    print(''.join(res))
remove_special_ch()

#9.Write a program to remove all white spaces from a string.
#i/p--'I am an engineer'
def remove_white_spaces():
    s=input('Enter a string: ')
    res=[char for char in s if not char==" "]
    print(''.join(res))
#remove_white_spaces()

#10.Write a program to extract values between quotation marks of a string.
#i/p--'He visited "chennai" ,"bangalore"'
#o/p--['chennai','bangalore']
def ext_values_quotation():
    s=input("enter a string")
    out=[]
    for i in s.split():
        if i.startswith('"')  and i.endswith('"'):
            i=i.replace('"',"")
            out.append(i)
    print(out)
#ext_values_quotation()

     
