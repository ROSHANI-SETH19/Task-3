def print_multiplication_table(n):
    print(f"Multiplication table for {n}:")
    for i in range(1, 11):
        product = n * i
        print(f"{n} x {i} = {product}")

# Input: An integer n
n = int(input("Enter a number: "))

# Output: Multiplication table
print_multiplication_table(n)
