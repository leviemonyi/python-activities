def is_prime(n):
    # A prime number is greater than 1 and has no divisors other than 1 and itself
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):  # Check divisibility up to the square root of n
        if n % i == 0:
            return False
    return True

def find_primes_in_range(start, end):
    # List comprehension to collect all prime numbers in the given range
    primes = [num for num in range(start, end + 1) if is_prime(num)]
    return primes

# Input: Range from the user
start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))

# Get all prime numbers in the range
primes = find_primes_in_range(start_range, end_range)

# Output: Print the prime numbers
print(f"Prime numbers between {start_range} and {end_range}: {primes}")
