from textsummerizer.logging import logging
from textsummerizer.exception import CustomException
import os
import sys

logging.info("HI")
# raise CustomException(sys,'e')

if __name__ == "__main__":

    try:
        a = 1/0
    except Exception as e:
        logging.info('Divided by zero')
        raise CustomException(e, sys)