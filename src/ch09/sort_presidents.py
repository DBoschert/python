
presidents = []

with open("presidents.txt", "r") as pres:

    for line in pres:
        fields = line.strip().split(":")
        presidents.append(fields)

for fields in sorted(presidents, key=lambda e: (e[1], e[2])):
    print(fields[2], fields[1], fields[6])

