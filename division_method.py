import math
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def find_factors(n):
    factors = []
    prime_factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
            if is_prime(i):
                prime_factors.append(i)
    return factors, prime_factors

number = int(input("Enter a number: "))
factors, prime_factors = find_factors(number)

print(f"Factors of {number}: {factors}")
print(f"Prime factors of {number}: {prime_factors}")
