import logging
import os
from datetime import datetime
from colorlog import ColoredFormatter

def setup(LOG_LEVEL = logging.INFO):
    LOGFORMAT = "%(log_color)s%(threadName)s%(reset)s : "\
                "%(log_color)s%(levelname)s%(reset)s | %(log_color)s%(" \
                "message)s%(reset)s "
    logging.root.setLevel(LOG_LEVEL)
    formatter = ColoredFormatter(LOGFORMAT)
    stream = logging.StreamHandler()
    stream.setLevel(LOG_LEVEL)
    stream.setFormatter(formatter)
    log = logging.getLogger(__name__)
    log.setLevel(LOG_LEVEL)
    log.addHandler(stream)

    if not os.path.exists('logs'):
        os.mkdir('logs')

    fh = logging.FileHandler(filename='logs/{}_{}.log'.format('ProgramWorker',
                             datetime.now().strftime('%m_%d_%y')))
    fh.setLevel(logging.INFO)
    log.addHandler(fh)
    return log