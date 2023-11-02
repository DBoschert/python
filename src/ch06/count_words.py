import sys

pattern = sys.argv[1]

for file_name in sys.argv[2:]:
    count = 0
    with open(file_name) as file_in:
        for line in file_in:
            if pattern in line:
                count += 1

    print(f"'{pattern}' was found on {count} lines in {file_name}")
