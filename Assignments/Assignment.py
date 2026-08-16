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

#11.Write a program to convert snake case string to camel case string.
#i/p--"user_name"
#o/p--"userName"
def snake_Camel():
    s=input("Enter the snake_case_string: ")
    b=s.split('_')
    for idx, val in enumerate(b):
        if idx != 0:
            b[idx] = val.capitalize()  

    print(''.join(b))
#snake_Camel()
#12.write a program to is year leap year or not.
#i/p--2024          i/p--2021
#o/p--Leap year     o/p--Not Leap year

def is_leap_year():
    year=int(input("Enter the year: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Leap year")
    else:
        print('Not Leap year')
#is_leap_year()

#13.Write a program to convert a string to datetime.
#i/p--'2026-08-16'
#o/p--2026-08-16

from datetime import datetime

def convert_string_to_date():
    date_str1 = "2026-08-16"
    format1 = "%Y-%m-%d"
    try:
        # strptime parses the string based on the provided format
        parsed_date = datetime.strptime(date_str1, format1)
        print( parsed_date.date())  # .date() extracts just the date component
    except ValueError as e:
        print( f"Error: The string does not match the format provided. Details: {e}")

#convert_string_to_date()

#14.Write a function that accepts a string and calculate the number of upper case letters and lower case letters.
#i/p--'Hyederabad,Chennai,Mumbai,Kolkatta,Pune'
#o/p--The number of uppercase characters:5
#     The numner of lowercase characters:30
def no_upper_lower():
    s=input("Enter the String:")
    upper=0
    lower=0
    for i in s:
        if i.isalpha():
            if i.isupper():
                upper+=1
            elif i.lower():
                lower+=1
            else:
                None
    print(f'The number of uppercase characters:{upper}')
    print(f'The numner of lowercase characters:{lower}')
#no_upper_lower()          
        
#15.Write a function that takes a list and returns a new list with unique elements of the first list.
#i/p--['Madurai',Chennai','Coimbatore','Kanyakumari','Madurai']
#o/p--List of unique elements ['Madurai','Chennai','Coimbatore','Kanyakumari']
def return_unique_list(): 
    l=list('Enter the list of elements: ')
    print(l)
    l=list(set(l))
    print('List of unique elements:',l)

#return_unique_list()

#16.17.Write a function that takes a number as a parameter and check the number is prime or not.
#i/p--17               25
#o/p--'It is a prime'  'It is non prime' 

def is_prime():
    a=int(input('Enter the number'))
    fact=0
    for i in range(1,a+1):
        if a%i==0:
            fact+=1
    if fact==2:
        print("It is a prime")
    else:
        print("It is a non prime")

#is_prime()

#17.Write a program to print the even numbers from a given list.
#i/p--[27,90,56,43,23,78]
#o/p--[90,56,78]

#num=list(input('Enter the list of natural numbers:'))
even=lambda x:True if x%2==0 else False
#even_numbers=list(filter(even,num))
#print(even_numbers)

#18.Write a function to check whether a number is perfect or not.
#i/p--6               24
#o/p--Perfect number  Not a perfect Number
def is_perfect():
    num=int(input("Enter the number:"))
    div=0
    for i in range(1,num):
        if num%i==0:
            div+=i
    print('Perfect' if num==div else 'Not a Perfect Number')
#is_perfect()

#19.Write a program to reverse a string word by word.
#i/p--'Python is easy to learn'
#o/p--'learn to easy is Python'
def reversed_sentence():
    s=input('Enter a sentence: ')
    out=[]
    for i in s.split()[::-1]:
        out.append(i)
    print(' '.join(out))

reversed_sentence() 
