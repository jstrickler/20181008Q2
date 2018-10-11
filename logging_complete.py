#!/usr/bin/env python
"""
Demonstration of complete logging configuration.
"""
import random
import logging
from randomwords import RandomWords

LEVELS = "debug info warning error critical".split()

def main():
    """
    Program entry point.

    :return: None
    """
    random_words = RandomWords()

    my_logger = logging.getLogger(__name__)

    logging.basicConfig(
        filename='montylogger.log',
        level=logging.INFO,
        format="%(name)s %(levelname)s %(asctime)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    my_logger.setLevel(logging.INFO)

    levels = [getattr(my_logger, level) for level in LEVELS]

    for _ in range(100):
        logger = random.choice(levels)
        logger('{} {} {}'.format(*random_words(3)))


if __name__ == '__main__':
    main()
