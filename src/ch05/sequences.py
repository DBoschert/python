ctemps = [-40, 0, 37, 75, 100]

fruits = [
    '    MANGO', 'Apple', '   peach   ', 'PLUM   ', '  Apricot',
    'BaNaNa', 'Persimmon   '
]

print("Temperatures:")
for temp in ctemps:
    fahrenheit = ((9 * temp) / 5) + 32
    print(f'{temp}C is {fahrenheit:.1f}F')
    
print()

print("Clean Fruits:")
clean_fruits = [f.strip().lower() for f in fruits]
print(clean_fruits)