def swap_numbers(a, b):
    print("Before swap: a =", a, "b =", b)
    a = a + b
    b = a - b
    a = a - b
    print("After swap: a =", a, "b =", b)

# Example usage:
a = 5
b = 10
swap_numbers(a, b)