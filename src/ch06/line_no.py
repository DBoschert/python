import sys

for fName in sys.argv[1:]:
    with open(fName) as file_in:
        for i, line in enumerate(file_in, 1):
            print("{:4d}: {}".format(i, line), end='')
