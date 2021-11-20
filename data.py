import numpy as np
from numpy.linalg import inv

data = np.array([[4,6], [3,5], [5,8], [7,12], [6,11]])

X = np.matrix([[1,i[0]] for i in data])
x_transpose = X.transpose(1,0)
print(f"Traspuesta de X: \n{x_transpose}\n")

A = x_transpose*X
print(f"X transpuesta * X: \n{A}\n")

A_inversed = inv(A)
print(f"Inversa de X transpuesta * X: \n{A_inversed}")

# Transpose X * Y
Y =  np.matrix([i[1] for i in data]).transpose(1,0)
B = x_transpose*Y

R = A_inversed*B
print(f"Resultado: \n{R}")

print(f"\nRegresion lineal: y = {round(R.item(1,0),5)}x + {round(R.item(0, 0),5)}")