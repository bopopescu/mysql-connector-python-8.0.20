import logging

DEBUG = True

logger = logging.getLogger('mysql-connector-python')
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(threadName)s - %(levelname)s - %(message)s')

if DEBUG == True:
    logger.setLevel(logging.DEBUG)
    stream_hander = logging.StreamHandler()
    stream_hander.setLevel(logging.DEBUG)
    stream_hander.setFormatter(formatter)
    logger.addHandler(stream_hander)
else:
    logger.setLevel(logging.INFO)
    file_handler = logging.handlers.RotatingFileHandler(
        filename="/tmp/mysql-connector-python.log", maxBytes=1024*1024*20, backupCount=5)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
