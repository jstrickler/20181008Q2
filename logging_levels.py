#!/usr/bin/env python

import logging

logging.basicConfig(
    filename='TEMP/levels.log',
    level=logging.ERROR,
) # <1>

logging.warning('This message will be logged') # <2>
logging.debug('This message will NOT be logged') # <3>
logging.error('This message will be logged') # <4>
