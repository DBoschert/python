
max = 50

primes = []

for n in range(2, max + 1):
    for m in range(2, n-1):
        if n % m == 0:
            break;
    else: 
        primes.append(n)

print(primes)