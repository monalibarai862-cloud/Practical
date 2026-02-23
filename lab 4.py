import numpy as np
identity_matrix = np.eye(4)
print("4x4 Identity Matrix:")
print(identity_matrix)


A = np.random.randint(1, 10, (3, 3))
B = np.random.randint(1, 10, (3, 3))

print("Matrix A:")
print(A)
print("Matrix B:")
print(B)

print("Addition of A and B:")
print(A + B)

print("Multiplication of A and B:")
print(np.dot(A, B))