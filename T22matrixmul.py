def multiply_matrices(matrixA, matrixB):
    # Check if matrices can be multiplied
    if len(matrixA[0]) != len(matrixB):
        raise ValueError("Number of columns in A must equal number of rows in B")

    # Initialize the result matrix with zeros
    result = [[0 for _ in range(len(matrixB[0]))] for _ in range(len(matrixA))]

    # Multiply elements row-by-column and sum for each position
    for i in range(len(matrixA)):
        for j in range(len(matrixB[0])):
            for k in range(len(matrixB)):
                result[i][j] += matrixA[i][k] * matrixB[k][j]

    return result

# Example usage:
matrixA = [[1, 2, 3], [4, 5, 6]]
matrixB = [[7, 8], [9, 10], [11, 12]]

print("Matrix A:")
for row in matrixA:
    print(row)

print("\nMatrix B:")
for row in matrixB:
    print(row)

result = multiply_matrices(matrixA, matrixB)
print("\nResult:")
for row in result:
    print(row)