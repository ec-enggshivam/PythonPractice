from threading import Thread,Lock,RLock
import threading

lock=Lock()
rlock=RLock()
def write_to_console(*args):
    #print('\n')
    while True:
#        print(lock.locked())
#        if lock.locked():
#            print("some other operation\n")
#        else:

            #lock.acquire()
        with rlock:
            for x in range(args[0],args[1]):
                print(x)
                with rlock:
                    print('second lock')
            print(threading.current_thread().getName(),">>>>>>>completed<<<<<<<")
        #raise a
        #lock.release()
        break



    #print('\n')

T1=Thread(target=write_to_console,args=(1,21))
T1.start()

T2=Thread(target=write_to_console,args=(21,41))
T2.start()

T1.join()
T2.join()
