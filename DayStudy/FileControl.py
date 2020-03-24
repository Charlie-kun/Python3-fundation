#File control

import os 

'''
#File list display
print(os.listdir('.'))     #Display current directory file list
print(os.listdir('../'))    #Display current parents directory file list
'''
'''
#File type display
def filetype(fpath):
    print(fpath, ':')
    if os.path.isfile(fpath):
        print('Regular file')
    if os.path.isdir(fpath):
        print('Directory')
    if os.path.isdir(fpath):
        print('Symbolic link')

flist=os.listdir('.')
for fname in flist:
    filetype(fname)
'''
'''
#File access display
def fileaccess(fpath):
    print(fpath, ':')
    if os.access(fpath, os.F_OK):    #File exists check
        print('Exists')
    else:
        return
    if os.access(fpath,os.R_OK):    #file read access check
        print('R')
    if os.access(fpath,os.W_OK):    #file write access check
        print('W')
    if os.access(fpath, os.X_OK):   #file access permission passable check
        print('X')
    print

flist=os.listdir('.')
for fname in flist:
    fileaccess(fname)
'''
'''
#File permission change
os.chmod('sample.txt', 777)    #ex. Linux case
'''
'''
#File name change
os.rename('t.txt', 't1.txt')     # name chage t.txt->t1.txt
print(os.access('t.txt', os.F_OK))
print(os.access('t1.txt', os.F_OK))
'''
'''
#File Move
os.rename('t1.txt', 'example/t1.txt')    #t1.txt move to "example" directory.
print(os.access('example/t1.txt', os.F_OK))
'''
'''
#file copy
import shutil
shutil.copyfile('sample.txt', 'sample_new.txt')    #file copy
print(os.access('sample_new.txt', os.F_OK))
'''
'''
#File path and exists check
print(os.getcwd())    #Current Working Directory
print(os.path.abspath('FileControl.py'))    #File Path

f=os.path.abspath('FileControl.py')
print(os.path.exists(f))
print(os.path.exists('FileControl.py'))
print(os.path.exists('adsf.txt'))
'''
'''
#Get a name for current/parents directory
print(os.curdir)    #current directory
print(os.pardir)    #parents directory
#Get a divide character
print(os.sep)
'''
'''
#Divide path name(File exist or not don't care)
f=os.path.abspath('FileControl.py')
print(os.path.basename(f))    #Display just file name
print(os.path.dirname(f))    #Display directory path
print(os.path.split(f))    #Display directory path divide to file name, for linux
#print(os.path.splitdrive(f))    #Display directory path divide to file name, for windows
print(os.path.splitext(f))    #Display file name divide to Extension name.
'''

#Directory Controll
'''
#Change directory
os.chidir('/User/name/Public')    #change working directory
'''
'''
#Create and delete directory
os.mkdir('temp')    #Directory create as standard mode "755"(rwxr-xr-x).
os.mkdir('temp', 700)    #Directory create as "700" mode(rwx-----).
print(os.access('/User/name/Public/temp'))

os.rmdir(temp)
print(os.access('/User/name/Public/temp'))    #Single level directory(in a no files) delete.

os.removedirs('/User/name/Public/temp')    #Stepped level directory(in a no files) delete.

import shutil
shutile.rmtree('temp')    #Directory delete everything.
'''
'''
#Directory copy
import shutil
os.mkdir('temp')
os.mkdir('temp/temp2', 700)
shutil.copytree('temp', 'myweb_backup')    #Copy to "temp" everything.
'''

#Directory research
'''
os.chdir('/User/name/Public')
print(os.getcwd())

for path, subdirs,files in os.walk(os.getcwd()):    #os.walk means under all tree directories.
    for fname in files:
        if fname.endswith('.pyc'):    #delete "*.pyc" files
            fullpath=os.path.join(path, fname)
            print('removing', fullpath)
            os.remove(fullpath)
'''

