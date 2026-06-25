4. Vectorized computing
import numpy as np
# Generate some random data
data = np.random.rand(1000)      # 1000 random numbers
# Example of vectorized operations
# Element-wise operations
result1 = np.sqrt(data)  # Square root of each element
result2 = np.sin(data)   # Sine of each element
result3 = data ** 2      # Square of each element
# Reduction operations
sum_data = np.sum(data)          # Sum of all elements
mean_data = np.mean(data)        # Mean of all elements
max_data = np.max(data)          # Maximum value
argmax_data = np.argmax(data)    # Index of maximum value
# Print some results for illustration
print(f"Square root of data: {result1}")
print(f"Sine of data: {result2}")
print(f"Square of data: {result3}")

print(f"Sum of data: {sum_data}")
print(f"Mean of data: {mean_data}")
print(f"Max value in data: {max_data}")
print(f"Index of max value in data: {argmax_data}")
