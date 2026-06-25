def is_prime(n):
  # If n is 1, it is not prime
  if n == 1:
    return False

  # Initialize a variable to keep track of the current divisor
  divisor = 2

  # While the current divisor is less than or equal to the square root of n, check if n is divisible by the divisor
  while divisor <= math.sqrt(n):
    if n % divisor == 0:
      return False
    divisor += 1

  # If n is divisible by no number from 2 to its square root, it is prime
  return True

# Get input from the user
n = int(input('Enter a number to check whether it is prime or not: '))

# Check if the number is prime
if is_prime(n):
  print(n, 'is a prime number.')
else:
  print(n, 'is not a prime number.')
