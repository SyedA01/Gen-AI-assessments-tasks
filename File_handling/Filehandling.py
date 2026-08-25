#creating file
f=open('Syed.txt','w+')
f.write('Python\n Machine learning\n DeepLearning\n Genarative AI\n')
f.close()

#reading file
f1=open('Syed.txt','r')
print(f1.read())
f1.close()
#reading size based
f2=open('Syed.txt','r')
print(f2.read(5))

#reading lines
f3=open('Syed.txt','r')
print(f3.readline())
print(f3.readlines())

#fetch type reading
f4=open('Syed.txt','r')
for i in f4.readlines():
    print(i)

#writing file
tech=['\nFastapi','\nMCP','\nRAG']
f5=open('Syed.txt','a+')
f5.writelines(tech)
f5.close()

f6=open('Syed.txt','r')
print(f6.readlines())