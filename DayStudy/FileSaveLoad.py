'''
File write, read
File save, load
'''
'''
import os

print(os.getcwd())    # Current Working Directory check.
'''
'''
#file write
s="""Its power : Python developers typically report they are able to develop applications in a half to a tenth the
amount of time it takes them to do the same work in such languages as C."""    #Passable to a lot line string because used """ """".
f=open('t.txt', 'w')    #File open t.txt, read only(w)
f.write(s)    #Save to string "s"
f.close()
'''
'''
#file read
f=open('t.txt')    #None select mode as "read mode"
s=f.read()    #So heavy work for memory
print(s)
f.close()    #Close File
'''
'''
#File Read line using 'for'
f=open('t.txt')
i=1
for line in f:
    print(i, ":", line)
    i+=1
f.close()
'''
'''
#File Read method
f=open('t.txt')
line=f.readline()    #readline method
i=1
while line:    #Repeat read line
    print(i, ":", line)
    line=f.readline()
    i+=1
f.close()
'''
'''
#ReadLines
f=open('t.txt')
print(f.readlines())
print()

f.seek(0)    #move pointer
i=1
for line in f.readlines():
    print(i,":", line)
    i+=1
f.close()
'''
'''
#XReadLines(python2)
f=open('t.txt')
print(f.xreadlines()
print()

f.seek(0)    #Move file pointer to start point
i=1
for line in f.xreadlines():
    print(i,":", line)
    i+=1
f.close()
'''
'''
#File writelines for each line
lines=['first line\n', 'second line\n', 'third line\n']    #"\n" is important
f=open('t1.txt', 'w')
f.writelines(lines)
f.close()

f=open('t1.txt')
print(f.read())
f.close()
'''
'''
#File write for each line
lines=['first line', 'second line', 'third line']
f=open('t1.txt', 'w')
f.write('\n'.join(lines))    #Each element chained to '\n'
f.close()

f=open('t1.txt')
print(f.read())
f.close()
'''
'''
#File write append
f=open('removeme.txt', 'w')
f.write('first line\n')
f.write('second line\n')
f.close()

f=open('removeme.txt', 'a')    #append
f.write('third line\n')
f.close()

f=open('removeme.txt')
print(f.read())
f.close()
'''

#File pointer
name='t.txt'
f=open(name, 'w+')   #Passable to read and write
s='012345689abcedf'
f.write(s)

f.seek(5)
print(f.tell())    #display for pointer's location
print(f.read(1))    #display for pointer's location char read
print(f.tell())    #read 1 char 