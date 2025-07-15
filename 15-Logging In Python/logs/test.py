from logger import logging

def add(a, b):
    logging.debug("Addition operation is taking place")
    return (a+b)

logging.debug("Addition fn is called")
add(12, 55)