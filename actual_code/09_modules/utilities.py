"""
This is a utilities module for my project.
"""
from datetime import datetime

print(datetime.now())




import logging
import logger
logger.logger.info("Hello from utilities.py")

def my_printer(message):
    print(f"Computer says {message}")

class Result:
    def __init__(self, result):
        self.result = result

result_1 = Result(1)

def main():
    my_printer(f"Hello from utilties.py. My name is {__name__}")

if __name__ == '__main__':
    main()