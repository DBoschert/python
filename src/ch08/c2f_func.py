
def c2f(celsius):
    celsius = float(celsius)
    fahrenheit = ((9 * celsius) / 5) + 32
    return fahrenheit


f = c2f(100)
print(f)