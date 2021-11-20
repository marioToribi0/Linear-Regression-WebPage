#import matplotlib.pyplot as plt  # To visualize
# import pandas as pd  # To read data
import csv
#from matplotlib.pyplot import axis
from sklearn.linear_model import LinearRegression
import datetime
import numpy as np
from numpy.linalg import inv
# data = pd.read_csv('HistoricalData_1634485094956.csv')  # load data set
# print(data["Date"])

X = []
Y = []

with open('static\data\companies\ZYNGACSV.csv', newline='') as csvfile:
    spamreader = csv.DictReader(csvfile)
    for row in spamreader:
        X.append(row["Date"])
        Y.append(row["Close/Last"])

# first_time = data.iloc[0, 0]
# X = data.iloc[:, 0].values.reshape(-1, 1)  # values converts it into a numpy array
# Y = data.iloc[:, 4].values.reshape(-1, 1)  # -1 means that calculate the dimension of rows, but have 1 column

# # Transform
for i in range(len(X)):
    # Date
    text = X[i].split("/")
    if (i==0):
        first_time = datetime.datetime(day=int(text[1]), month=int(text[0]), year=int(text[2]))
    actual_time = datetime.datetime(day=int(text[1]), month=int(text[0]), year=int(text[2]))

    X[i] = abs((actual_time-first_time).days)
    # Price
    Y[i] = float(Y[i].split("$")[1])

X = np.array(X, dtype="int")
Y = np.array(Y, dtype="float")
X = X.reshape(-1,1)
Y = Y.reshape(-1,1)

linear_regressor = LinearRegression()  # create object for the class
linear_regressor.fit(X, Y)  # perform linear regression
Y_pred = linear_regressor.predict(X)  # make predictions

new_Y = list(map(lambda x: x[0], Y_pred))
# Y = list(map(lambda x: x[0], Y))
# X = list(map(lambda x: x[0], X))
print(linear_regressor.coef_)
print(linear_regressor.intercept_)

# print(new_Y[:15])
# print(Y[:15])
# #print([i for i in range(25)])

# plt.scatter(X, Y)
# plt.plot(X, Y_pred, color='red')
# plt.show()

data = np.empty((len(X), 0), float)
data = np.append(data, X, axis=1)
data = np.append(data, Y, axis=1)

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