import utilities as u
from utilities import my_printer as p
from logger import logger

# import numpy as np
# import pandas as pd

logger.info("Hello from app.py")
u.my_printer("Hello from app.py")
p("This is me being very lazy!")
print(__name__)
print(__doc__)

u.logging.basicConfig(level=u.logging.DEBUG)

import pprint

leo = {
                "name":"Leonardo",
               "country":"Italy",
               "city": "Udine",
               }

print(leo)
pprint.pprint(
    leo,
    indent=4,
)

from cern.mathematics import add



print(f"Add 4 and 5, {add(4, 5)}")