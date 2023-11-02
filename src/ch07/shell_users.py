shells = {}
with open("passwd") as passwd_in:
    for line in passwd_in:
        shell = line.strip().split(":")[-1]

        if shell not in shells:
            shells[shell] = 0

        shells[shell] += 1

for shell, count in shells.items():
    if len(shell.strip()) > 0:
        print(f"{count} {shell}")
