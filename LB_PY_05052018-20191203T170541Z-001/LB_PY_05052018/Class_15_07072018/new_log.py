
import logging
import sys
#currentfuncName = lambda n=0 : sys._getframe(n+1).f_code.co_name
logging.basicConfig(format='Time:%(asctime)s %(levelname)s:%(message)s (File:%(filename)s Func:%(funcName)s Line:%(lineno)d)',filename='example.log',level=logging.DEBUG)

logging.debug('This is debug message should go to the log file')
logging.info('This message is information')
logging.warning('This message is warning')
logging.error("This is error message")
logging.critical("This is critical message")


def sample_fun():
    logging.debug('This is debug message from function sample_fun')

sample_fun()


