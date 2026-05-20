def my_function():
    raise ValueError("Something went wrong.")


try:
    my_function()
    print("No error reported.")
except SyntaxError:
    print("Something went wrong.")
except ValueError:
    print("Something went wrong.")