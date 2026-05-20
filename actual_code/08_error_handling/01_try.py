import traceback
import logging

logging.basicConfig(filename="error.log",
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger()

logger.info("Program starting.")
# risky: users, connection, data, anything we don't have control over!
user_input = input("Please enter a number: ")
try:
    result = int(user_input)
    print(100/result)
    open("thisfiledoesnotexist")
except ValueError:
    print("You tried to convert something that wasn't a number.")
    logger.error(traceback.format_exc())
except ZeroDivisionError:
    print("You tried to divide by zero.")
except Exception:
    print("Something went wrong.")
    logger.critical(traceback.format_exc())

logging.info("Program finished.")