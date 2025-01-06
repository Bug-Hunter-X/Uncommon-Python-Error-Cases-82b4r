def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    return sum(numbers) / len(numbers)

my_list = []
result = calculate_average(my_list)
print(f"The average is: {result}")

#Another case of error
def process_data(data):
    try:
        value = int(data['value'])
        return value * 2
    except (KeyError, ValueError) as e:
        print(f"Error processing data: {e}")
        return None

data = {"name":"John"}
result = process_data(data)
print(f"Result is: {result}")

#Another case of error

def my_function(x):
  if x < 0:
    raise ValueError("Input must be non-negative")
  return x * 2

# Example usage
try:
  result = my_function(-5)
  print(f"The result is: {result}")
except ValueError as e:
  print(f"Error: {e}")