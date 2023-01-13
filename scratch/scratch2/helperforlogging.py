import logging
logger = logging.getLogger(__name__)
logger.propagate= False # The default is True, this is an optional config.
logger.info('Hello from helper')
