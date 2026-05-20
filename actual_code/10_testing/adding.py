def add(a,b):
    if not isinstance(a, (int, float)) or isinstance(a, bool):
        raise TypeError("a must be a number")
    if not isinstance(b, (int, float)) or isinstance(a, bool):
        raise TypeError("b must be a number")
    return a + b
