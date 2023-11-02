from temp_conv import c2f

temp_str = input("Enter Celsius: ")
celsius = float(temp_str)
fahrenheit = c2f(celsius)

print(f"{celsius}C is {fahrenheit}F")

