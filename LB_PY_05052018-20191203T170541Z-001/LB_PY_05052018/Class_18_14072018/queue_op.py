from queue import Queue,LifoQueue

'''
q1=Queue()
q1.put(5)
q1.put(6)

print(q1.get())
print(q1.get())
#print(q1.get())
'''

q2=LifoQueue()
q2.put(5)
q2.put(6)
print(q2.get())
print(q2.get())
print(q2.get())


