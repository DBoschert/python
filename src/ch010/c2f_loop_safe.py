while True:
        
    celsius = input('Enter Celsius: ')
    if celsius == '':
        continue
    if celsius.lower().startswith('q'):
        break
    try:
        celsius = float(celsius)
    except Exception:
        print("ONLY ENTER NUMBERS")
        print("number was automatically entered as 1")
        celsius = 1
    fahrenheit = ((9 * celsius) / 5) + 32
    print(f'{celsius:.1f}C is {fahrenheit:.1f}F\n')