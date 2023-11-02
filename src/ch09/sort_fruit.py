with open("fruit.txt", "r") as F:
    fruit_lines = F.readlines()

print("Sorted by Default")
print("".join(sorted(fruit_lines)))
print()

print("Sorted by Case Insensitive")
print("".join(sorted(fruit_lines, key = str.lower)))
print()

print("Sorted by Length of Name")
print("".join(sorted(fruit_lines, key=lambda s: (len(s), s.lower()))))
print()

print("Sorted by Second Letter then First Letter")
print("".join(sorted(fruit_lines, key=lambda s: (s[1].lower(), s[0].lower()))))
print()
