import numpy as np

# Example 1: Scalar + Array
a = np.array([1, 2, 3])
print("a:", a)
print("a + 5:", a + 5)
print()

# Example 2: Row vector + 2D Array
A = np.array([[1, 2, 3],
              [4, 5, 6]])
B = np.array([10, 20, 30])
print("A:\n", A)
print("B:", B)
print("A + B:\n", A + B)
print()

# Example 3: Column vector + Row vector (outer sum)
C = np.array([[1],
              [2],
              [3]])
D = np.array([10, 20, 30])
print("C:\n", C)
print("D:", D)
print("C + D:\n", C + D)
print()

# Example 4: Broadcasting multiplication
E = np.array([[1, 2, 3],
              [4, 5, 6]])
F = np.array([[2],
              [3]])
print("E:\n", E)
print("F:\n", F)
print("E * F:\n", E * F)
