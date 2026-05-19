# define ...
name = "Kevin"
def print_message_with_borders(message, border_symbol="=", border_length=10):
    """
    A function that prints a message with a border_symbol and a border_length.
    :param message: The message to print
    :param border_symbol: The border_symbol to print
    :param border_length: The border_length to print
    :return:
    """
    print(border_symbol * border_length)
    print(message)
    print(border_symbol * border_length)

# called/invoked
message = "Namibia is better than SA!"
length = len(message)

print_message_with_borders(message, border_length=length)
print_message_with_borders(border_length=15, message="Germany is great!", border_symbol="@")
print_message_with_borders("Brazil is great!", "&", 20)
print(print_message_with_borders("Hello", "{}", 20))

def get_message_with_borders(message, border_symbol="=", border_length=10):
    """
    A function that creats a message with a border_symbol and a border_length.
    :param message: The message to print
    :param border_symbol: The border_symbol to print
    :param border_length: The border_length to print
    :return:
    """
    result = f"""{border_symbol * border_length}
{message}
{border_symbol * border_length}"""
    return result

print(get_message_with_borders("Python is great!").upper())

print(sum([1,2,3], start=10))