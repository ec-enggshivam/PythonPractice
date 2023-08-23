from threading import Thread
import threading as td
import time


def write_file(*args):
    print(td.current_thread())
    print('\n')
    print(td.get_ident())
    td.current_thread().setName(args[2])
    fileobj=open(args[0],"w")
    for x in range(args[1]):
        fileobj.write(str(x))
        fileobj.write('\n')

    fileobj.close()
    print('\n')
    print(td.current_thread())
    time.sleep(100)
    print(td.current_thread().getName(),">>>>>completed<<<<<<\n")


filename1=input("Enter the file name")
T1=Thread(target=write_file,args=(filename1,1000,"sample1"))
T1.start()

filename2=input("Enter the file name")
T2=Thread(target=write_file,args=(filename2,1000,"sample2"))
T2.start()

print(td.get_ident())
print(td.current_thread())
print(td.current_thread().getName())

T1.join()
T2.join()
print(">>>Task Completed<<<")



