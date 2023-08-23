import os
from shutil import copyfile

def CopyConfig(src,dst):
    copyfile(src,dst)

def ChangeConfig(src,param,old,new):
    fileobj=open(src,"r")
    lines=fileobj.readlines()
    fileobj.close()
    fileobj=open(src,"w")
    oldvalue=param+"="+old
    newvalue = param+"="+new

    for line in lines:
        line=line.replace(oldvalue,newvalue)
        fileobj.write(line)
    fileobj.close()

def AppendConfig(src,str):
    val=str+'\n'
    fileobj = open(src, "a+")
    print(val)
    fileobj.write(val)
    fileobj.close()

def DeleteConfig(src,str):
    fileobj = open(src, "r")
    lines = fileobj.readlines()
    fileobj.close()
    fileobj = open(src, "w")
    val=str+'\n'
    for line in lines:
        if(line!=val):
            fileobj.write(line)
    fileobj.close()