# Check whether a given number is prime or not Using for and if statements
import math
def is_prime(n):
  # If n is 1, it is not prime
  if n == 1:
    return False
  # Iterate from 2 to the square root of n
  for i in range(2, int(math.sqrt(n)) + 1):
    # If n is divisible by any number from 2 to its square root, it is not prime
    if n % i == 0:
      return False
  # If n is divisible by no number from 2 to its square root, it is prime
  return True
# Get input from the user
n = int(input('Enter a number to check whether it is prime or not: '))
# Check if the number is prime
if is_prime(n):
  print(n, 'is a prime number.')
else:
  print(n, 'is not a prime number.')
