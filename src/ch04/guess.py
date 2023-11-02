# Can do this in python:
# min, max = 1, 26

print("Enter 'l': Guess is too low")
print("Enter 'h': Guess is too high")
print("Enter 'y': Guess is the Correct answer")
print("Enter 'q' to quit")
print()

max = input("Enter Max Value: ")
min = input("Enter Minimum Value: ")
max = int(max)
min = int(min)
count = 0;

while True:
    guess = (max + min) // 2
    answer = input(f"Is {guess} your number? ")

    if answer == "q":
        break

    if answer == "h":
        max = guess
    elif answer == "l":
        min = guess
    elif answer == "y":
        print("I guessed it!")
        print(f"Guessed in {count} tries")
        break
    else:
        print("Please enter 'h', 'l', or 'y'")
    if(answer == "h" or answer == "l"):
        count += 1;
    