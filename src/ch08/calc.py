
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


while True:
    answer = input("Do Maths: ")

    if answer.lower() == 'q':
        break

    n1, op, n2 = answer.split()
    n1 = float(n1)
    n2 = float(n2)

    if op == '+':
        result = add(n1, n2)
    elif op == '-':
        result = subtract(n1, n2)
    elif op == '*':
        result = multiply(n1, n2)
    elif op == '/':
        result = divide(n1, n2)
    else:
        print("Error!")
        continue
    
    print(f"{result:.2f}")
