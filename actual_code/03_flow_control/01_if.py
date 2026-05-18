user_color = input("Give me a colour:").lower().strip()
if user_color == "white":
    print("Light is white when it hasn't been split!")
elif user_color == "black":  # elif is a contraction of else if
    print("Black is the absence of light!")
elif user_color == "red":
    print("Red is a primary colour")
elif user_color == "green":
    print("Grass is green.")
elif not user_color.startswith("g"):
    print("Did you mean green or gold?")
elif user_color == "blue" or user_color.startswith("q"):
    print("Did you mean blue or blue?")

else:
    print("I don't know that colour.")

