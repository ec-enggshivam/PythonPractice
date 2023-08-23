import threading
#import queue

e = threading.Event()
e1= threading.Event()
e2= threading.Event()

def print_11to20():
    tname = threading.current_thread().name
    print ('Thread waiting for event: %s' % tname)
    e.wait()
    print ('Thread got event: %s' % tname)
    for x in range(11, 21):
        print("in side print_11to20",x)

def print_1to20():
    tname = threading.current_thread().name
    for x in range(1,21):
        if x<11:
            print("in side print_1to20",x)
        else:
            data=input("Hit enter to set the event")
            e.set()


t1 = threading.Thread(target=print_11to20) #11 to 20
t1.start()
t2 = threading.Thread(target=print_1to20) #1 to 10
t2.start()

e.clear()
t1.join()
t2.join()
print ('All done.')
