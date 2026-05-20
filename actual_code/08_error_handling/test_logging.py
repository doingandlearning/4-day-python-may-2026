import logging
import traceback

logging.basicConfig(filename="error.log",
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger()

class Customer:
  def __init__(self, name, contact_email):
    if len(name) == 0:
      logging.error("Name cannot be empty")
      raise ValueError("You need to give me a name.")
    self.name = name
    self.contact_email = contact_email

  def send_confirmation(self, booking):
    print(f"Sending {booking} confirmation to {self.contact_email}")

customer = Customer("", "")