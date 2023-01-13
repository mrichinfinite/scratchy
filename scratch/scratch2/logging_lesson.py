# Logging in Python: https://docs.python.org/3/howto/logging.html
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S')
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

#It's best practice to create your own logging module and not to use 'root' as shown above. Therefore we will import our own logging module here.
import helperforlogging

# Now you can set different log handlers like this.
logger = logging.getLogger(__name__)

# Create handler
stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')

# Level and format
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

# A separate file of file.log will populate in our dir after running this.
logger.warning('This is a warning')
logger.error('This is an error')

# We can import from a conf file if we want as well. Let's see how this works.
import logging.config

logging.config.fileConfig('logging.conf')

logger = logging.getLogger('simpleExample')
logger.debug('This is a debug message')
# You can also use the dictConfig() method as well, refer to the documentation for more info on that.

''''''

# Stack tracer
try:
    a = [1,2,3]
    val = a[4]
except IndexError as e:
    logging.error(e, exc_info=True)
# This is helpful for troubleshooting issues.

# Here's another way of doing the above.
import traceback
try:
    a = [1,2,3]
    val = a[4]
except:
    logging.error('The error is %s', traceback.format_exc())

# Rotating file handler
'''If you have a large app with a lot of log messages and you want to keep track of the most recent events, 
then you can use a rotating file handler that keeps the files small'''

from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Name of log file, then roll over after 2KB, and keep backup logs app.log.1, app.log.2, etc. Finally, set backup counts.
handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)
logger.addHandler(handler)

for _ in range(10000):
    logger.info('Hello world!')

# You can also do the same as above but specify a rollover after an allotted time has passed.
from logging.handlers import TimedRotatingFileHandler
import time

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Specify when when it should rollover using s, m, h, d, midnight, w0, w1, w2, etc.
handler = TimedRotatingFileHandler('timed_test.log', when='s', interval=1, backupCount=5)
logger.addhandler(handler)

for _ in range(6):
    logger.info('Hello world!')
    time.sleep(5)

'''If you have a lot of different modules and are logging a lot of data (like if you use a microservice architecture),
then it's recommended to use JSON format for logging. See here for more: https://github.com/madzak/python-json-logger'''