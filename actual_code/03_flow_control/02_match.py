user_color = input("Give me a colour:").lower().strip()
if user_color == "white":
    print("Light is white when it hasn't been split!")
elif user_color == "black":  # elif is a contraction of else if
    print("Black is the absence of light!")
elif user_color == "red":
    print("Red is a primary colour")
elif user_color == "green":
    print("Grass is green.")
else:
    print("I don't know that colour.")

match user_color:
    case "white":
        print("Light is white when it hasn't been split!")
    case "black":
        print("Black is the absence of light!")
    case "red":
        print("Red is a primary colour")
    case "green":
        print("Grass is green.")
    case _:
        print("I don't know that colour.")