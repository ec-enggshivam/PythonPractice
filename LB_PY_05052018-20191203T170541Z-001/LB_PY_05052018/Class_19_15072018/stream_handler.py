import logging
import sys


LOG_FILENAME = 'logging.log'
h = logging.StreamHandler(sys.stdout)
logger=logging.getLogger("sample")
logger.addHandler(h)
f=open(LOG_FILENAME,'a')
fh = logging.StreamHandler(f)
logger.addHandler(fh)


logger.setLevel(logging.DEBUG)


logger.debug('This is debug message should go to the log file')
logger.info('This message is information')

logger.warning('This message is warning')
logger.error("This is error message")
logger.critical("This is critical message")


logger.removeHandler(h)
logger.debug('This is second debug message should go to the log file')
logger.info('This message is second information')





'''
import logging

logger = logging.getLogger() # this gets the root logger
# ... here I add my own handlers 
logger.removeHandler(sys.stdout)
#logger.removeHandler(sys.stderr)

print(logger.handlers )
# this will print [&lt;logging.StreamHandler instance at ...&gt;]
# but I may have other handlers there that I want to keep

logger.debug("bla bla")
'''

'''

FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
logging.basicConfig(format=FORMAT)
d = {'clientip': '192.168.0.1', 'user': 'fbloggs'}
logger = logging.getLogger('tcpserver')
logger.warning('Protocol problem: %s', 'connection reset', extra=d)


would print something like


2006-02-08 22:20:02,165 192.168.0.1 fbloggs  Protocol problem: connection reset


'''