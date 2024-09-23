def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

# Example:
num_list = [10, 15, 23, 4, 17, 30, 2]
primes = filter_prime(num_list)
print(primes)  