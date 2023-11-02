from temp_conv import c2f

while True:
    uInput = input('Enter Celsius: ')
    if uInput.lower() == 'q':
        break
    if uInput == '':
        continue
    celsius = float(uInput)
    fahrenheit = c2f(celsius)
    print(f"{celsius}C is {fahrenheit}F")
    print()
