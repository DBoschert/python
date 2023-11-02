while True:
    celsius = input('Enter Celsius: ')
    if celsius == '':
        continue
    if celsius.lower().startswith('q'):
        break

    celsius = float(celsius)
    fahrenheit = ((9 * celsius) / 5) + 32
    print(f'{celsius:.1f}C is {fahrenheit:.1f}F\n')