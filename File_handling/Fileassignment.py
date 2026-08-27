name='Syed'
def ratrow():
    f=open('pattern.txt','w+')
    f.write("Right angle Triangle\n")
    for i in range(1,6):
        for j in range(0,i):
            f.write(str(i))
        f.write('\n')
    f.close()

def ratcol():
    f=open('pattern.txt','w+')
    f.write("Right angle Triangle-columnwise\n")
    for i in range(1,6):
        for j in range(0,i):
            f.write(str(j))
        f.write('\n')
    f.close()

def starpattern():
    f=open('pattern.txt','a+')
    f.write("Right angle Triangle column-wise\n")
    for i in range(1,6):
        for j in range(1,i+1):
            f.write('*')
        f.write('\n')
    f.close()

def chrctsrowup():
    f=open('pattern.txt','a+')
    f.write("Right angle Triangle characters-upper-rowwise\n")
    for i in range(1,6):
        for j in range(1,i+1):
            f.write(chr(i+64))
        f.write('\n')
    f.close()

def chrctsrowlower():
    f=open('pattern.txt','a+')
    f.write("Right angle Triangle characterslowercase-rowwise\n")
    for i in range(1,6):
        for j in range(0,i):
            f.write(chr(i+96))
        f.write('\n')
    f.close()

def chrctscolup():
    f=open('pattern.txt','a+')
    f.write("Right angle Triangle charactersuppercase-columnwise\n")
    for i in range(1,6):
        for j in range(0,i):
            f.write(chr(j+65))
        f.write('\n')
    f.close()
   
def chrctscollower():
    f=open('pattern.txt','a+')
    f.write("Right angle Triangle characterslowercase-columnwise\n")
    for i in range(1,6):
        for j in range(0,i):
            f.write(chr(j+97))
        f.write('\n')
    f.close()
def namerow():
    f=open('pattern.txt','a+')
    f.write("Right angle Triangle characterslowercase-rownwise\n")
    for i in range(0,len(name)):
        for j in range(0,i+1):
            f.write(name[i])
        f.write('\n')
    f.close()
def namecol():
    f=open('pattern.txt','a+')
    f.write("Right angle Triangle characterslowercase-columnwise\n")
    for i in range(0,len(name)):
        for j in range(0,i+1):
            f.write(name[j])
        f.write('\n')
    f.close()
def iratrow():
    f=open('pattern.txt','a+')
    f.write("Inverse Right angle Triangle\n")
    for i in range(5,0,-1):
        for j in range(0,i):
            f.write(str(i))
        f.write('\n')
    f.close()

def iratcol():
    f=open('pattern.txt','a+')
    f.write("Inverse Right angle Triangle-columnwise\n")
    for i in range(5,0,-1):
        for j in range(i,0,-1):
            f.write(str(j))
        f.write('\n')
    f.close()

def iratstar():
    f=open('pattern.txt','a+')
    f.write("Inverse Right angled Triangle star\n")
    for i in range(5,0,-1):
        for j in range(i,0,-1):
            f.write('*')
        f.write('\n')
    f.close()

def iratrowupper():
    f=open('pattern.txt','a+')
    f.write("Inverse Right angle Triangle upper-row\n")
    for i in range(5,0,-1):
        for j in range(0,i):
            f.write(chr(i+64))
        f.write('\n')
    f.close()

def iratrowlow():
    f=open('pattern.txt','a+')
    f.write("Inverse Right angle Triangle lower-row\n")
    for i in range(5,0,-1):
        for j in range(0,i):
            f.write(chr(i+96))
        f.write('\n')
    f.close()

def iratcolupper():
    f=open('pattern.txt','a+')
    f.write("Inverse Right angle Triangle upper-columnwise\n")
    for i in range(5,0,-1):
        for j in range(i,0,-1):
            f.write(chr(j+64))
        f.write('\n')
    f.close()

def iratcollow():
    f=open('pattern.txt','a+')
    f.write("Inverse Right angle Triangle lower-columnwise\n")
    for i in range(5,0,-1):
        for j in range(i,0,-1):
            f.write(chr(j+96))
        f.write('\n')
    f.close()

def iratnamerow():
    f=open('pattern.txt','a+')
    f.write("Inversed Right angle Triangle characters-rowwise\n")
    for i in range(len(name),0,-1):
        for j in range(0,i):
            f.write(name[i-1])
        f.write('\n')
    f.close()
def iratnamecol():
    f=open('pattern.txt','a+')
    f.write("Inversed Right angle Triangle characters-columnwise\n")
    for i in range(len(name),0,-1):
        for j in range(0,i):
            f.write(name[j])
        f.write('\n')
    f.close()

if __name__=='__main__':
    ratrow()
    ratcol()
    starpattern()
    chrctsrowup()
    chrctsrowlower()
    chrctscolup()
    chrctscollower()
    namerow()
    namecol()
    iratrow()
    iratcol()
    iratstar()
    iratrowupper()
    iratrowlow()
    iratcolupper()
    iratcollow()
    iratnamerow()
    iratnamecol()


