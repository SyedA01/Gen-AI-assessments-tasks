Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # string handling management
>>> # categories
... # ----------
... 
... # string operations (indexing / slicing / ranging)
... # string methods (concatenation / repetition / formatting)
... # string supporting functions(string dotted functions)
... 
... # string operations
... # -----------------
... # string = sequence of characters
... # string are enclosed with quotations
>>> 
>>>  name = 'syed'
...  
SyntaxError: unexpected indent
>>> name='syed'
>>> name
'syed'
>>> # syed
>>> # 0123
>>> # indexing = getting a particular character from a string using its INDEX value
... name[0]
's'
>>> name[1]
'y'
name[2]
'e'
name[3]
'd'
name[4]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    name[4]
IndexError: string index out of range
# this process is called STRING TRAVERSING / POSITIVE INDEXING

# r a j e s h
#-6-5-4-3-2-1

# NOTE: space is meaningful in python as it takes a index value
n
Traceback (most recent call last):
  File "<pyshell#13>", line 7, in <module>
    n
NameError: name 'n' is not defined

name[-1]
'd'
name[-2]
'e'
name[-3]
'y'
name[-4]
's'
# slicing = getting a particular portion from a string using (starting : stopping)
name[1:3]#12
'ye'
name[0:5]
'syed'
name[4:5]
''
name[3:4]
'd'
# string reverese
# ----------------
name[::-1]
'deys'
name
'syed'
name[-4:0]
''
name[-4:-2]
'sy'
name[::2]
'se'
name[::3]
'sd'
name[::-2]
'dy'
# ranging = almost similar to slicing
name='manju nathan'
name
'manju nathan'
name[:5]
'manju'
name[5:]
' nathan'
name='hepzibah vinithra rk'
name
SyntaxError: multiple statements found while compiling a single statement
KeyboardInterrupt
name='hepzibah vinithra rk'
name[:-15]
'hepzi'
name[-19:-15]
'epzi'
KeyboardInterrupt
name[-20:-15]
'hepzi'
name[9:14]
'vinit'
name[9:13]
'vini'
# string methods(concatenation / repetition / formatting)

name='rajesh'
age=41
city='dindigul'
#concatenation
name+city
'rajeshdindigul'
name+age
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    name+age
TypeError: can only concatenate str (not "int") to str
10+10
20
'10'+'10'
'1010'
name+str(age)
'rajesh41'
# repetition

name
'rajesh'
name*5
'rajeshrajeshrajeshrajeshrajesh'
# formatting
# ----------

# manual formatting
name
'rajesh'
age
41
city
'dindigul'
print('my name is {0} from {1} aged {2}'.format(name,city,age))
my name is rajesh from dindigul aged 41
print('my name is {} from {} aged {}'.format(name,city,age))
my name is rajesh from dindigul aged 41
print('my name is {} from {} aged {}'.format(name,age,city))
my name is rajesh from 41 aged dindigul
# automated formatting
print('my name is %s from %s aged %d' % (name,city,age))
my name is rajesh from dindigul aged 41
print('my name is %s from %s aged %s' % (name,city,age))
my name is rajesh from dindigul aged 41
print('my name is %s from %s aged %s' % (name,city,age))
my name is rajesh from dindigul aged 41
#general formatting
print('name is',name)
name is rajesh
print('name is',name,'hometown is',city)
name is rajesh hometown is dindigul
#formatted string
print(f'my name is {name} age is {age}'}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
print(f'my name is {name} age is {age}')
my name is rajesh age is 41

#string supporting functions/dotted function--->dedicated string methods
name.capitalize()
'Rajesh'
name.casefold()
'rajesh'
name.upper()
'RAJESH'
name.find('J')
-1
name.find('j')
2
name.index('s')
4
name.index('k')
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    name.index('k')
ValueError: substring not found
name.center()
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    name.center()
TypeError: center expected at least 1 argument, got 0
name.center(25)
'          rajesh         '
name.ljust(25)
'rajesh                   '
name.rjust(25)
'                   rajesh'
'130'.zfill(10)
'0000000130'
'130'.center(10,'*')
'***130****'
'syed '.strip()
'syed'
'syed abdul'.partition(' ')
('syed', ' ', 'abdul')
name.count('a')
1
name.endswith('h')
True
name.endswith('s')
False
name.startswith('r')
True
'-'.join(['syed','abdul'])
'syed-abdul'
'/'.join(['25','sept','2025'])
'25/sept/2025'
name.removeprefix('ra')
'jesh'
name.removesuffix('sh')
'raje'
'Syed abdul'.title()
'Syed Abdul'
'Syed abdul'.replace('a','A')
'Syed Abdul'
'Syed Abdul'.split()
['Syed', 'Abdul']
#check availability of string
name.isalnum()
True
'Syed123 '.isalnum()
False
name.isascii()
True
name.isdecimal()
False
'456'.isnumeric()
True
'567'.isdigit()
True
' ken'.isidentifier()
False
'ken2'.isidentifier()
True
'syed'.lower()
'syed'
' syed'.isspace()
False
' '.isspace()
True
