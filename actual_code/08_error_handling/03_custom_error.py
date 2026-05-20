import logging
import traceback

logging.basicConfig(filename="error.log",
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger()
user_input = input("Give me a positive number: ")

class NegativeNumberError(Exception):
    pass

try:
    user_input = int(user_input)
    if user_input < 0:
        raise NegativeNumberError("Number must be positive.")
    # doing something here that having a negative would break!
except ValueError:
    print("Not all of those characters were digits.")
except NegativeNumberError:
    print("Number must be positive.")
    logging.info(traceback.format_exc())

print(f"The user's input is {user_input}")