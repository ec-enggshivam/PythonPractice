import logging

def sample(m):
    logging.debug('sample started...')
    for i in range(m):
        print ('value of i= ',i)

    logging.debug('end of sample')

logging.basicConfig(format='Time:%(asctime)s %(levelname)s:%(message)s (File:%(filename)s Func:%(funcName)s Line:%(lineno)d)',filename='example4.log',level=logging.DEBUG)
logging.debug('main app starts here...')

a=input("Enter first Value")
logging.info('This message is information,value of a is '+ a)
a=int(a)

b=input("Enter Second Value")
logging.info('This message is information,value of b is '+ b)
b=int(b)



sample(b-a)

for j in range(a,b):
  print ('value of j=',j)

logging.info('end of the app')
'''
logging.debug('This is debug message should go to the log file')
logging.info('This message is information')
logging.warning('This message is warning')
logging.error("This is error message")
logging.critical("This is critical message")


def sample_fun():
    logging.debug('This is debug message from function sample_fun')

sample_fun()
'''

