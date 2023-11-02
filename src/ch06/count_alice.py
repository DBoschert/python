count = 0
with open("alice.txt") as alice_in:
    for line in alice_in:
        if "Alice" in line:
            count += 1

print(f"Alice was found on {count} lines")
