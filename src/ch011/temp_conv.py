def c2f(celsius):
    celsius = float(celsius)
    fahrenheit = ((9 * celsius) / 5) + 32

    return fahrenheit

def f2c(fahrenheit):
    fahrenheit = float(fahrenheit)
    celsius = (fahrenheit - 32) * (5.0 / 9)

    return celsius


# -----------------------


def a():
    pass

if __name__ == "__main__":
    a()
    print("Im running my module myself")
    print("this will be ignored if someone else besides me is running this module")