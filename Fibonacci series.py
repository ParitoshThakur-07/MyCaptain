def fibonacci(n):
    # Initialize the first two terms of the Fibonacci sequence
    a, b = 0, 1
    sequence = []

    # Generate Fibonacci sequence up to n terms
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b

    return sequence

# Input: Number of terms
num_terms = int(input("Enter the number of terms: "))

# Output: Fibonacci series
if num_terms <= 0:
    print("Please enter a positive integer.")
else:
    print(f"Fibonacci series up to {num_terms} terms:")
    print(fibonacci(num_terms))
