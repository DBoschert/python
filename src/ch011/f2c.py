from temp_conv import f2c

temp_str = input("Enter Fahrenheit: ")
fahrenheit = float(temp_str)
celsius = f2c(fahrenheit)

print(f"{fahrenheit}F is {celsius}C")