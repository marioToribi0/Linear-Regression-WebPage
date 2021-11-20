from enum import unique
from flask import Flask, request, render_template, redirect
import csv
from sklearn.linear_model import LinearRegression
import datetime
import numpy as np
import json

app = Flask(__name__)

# Get data
with open("static/data/company.json", encoding='utf-8') as file:
    all_companies = json.load(file)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/info")
def info():
    position = int(request.args['id'])-1
    company = all_companies[position]

    file = company["data"]
    
    X = []
    Y = []
    time = []
    close = []
    volume = []
    _open = []
    high = []
    low = []

    with open(f"static/data/companies/{file}", newline='') as csvfile:
        spamreader = csv.DictReader(csvfile)
        for row in spamreader:
            X.append(row["Date"])
            Y.append(row["Close/Last"])
            time.append(row["Date"])
            close.append(row["Close/Last"])
            volume.append(row["Volume"])
            _open.append(row["Open"])
            high.append(row["High"])
            low.append(row["Low"])
    
    # Data
    data = {
        "time": time,
        "close": close,
        "volume": volume,
        "open": _open,
        "high": high,
        "low": low
    }

    # Transform
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

    Y = list(map(lambda x: x[0], Y))
    Y_pred = list(map(lambda x: x[0], Y_pred))
    lineal_Y = Y_pred
    lineal_X = X

    return render_template("data.html", data=data,Y_pred=Y_pred, Y=Y, lineal_X=lineal_X, lineal_Y=lineal_Y, company=company, size=[i for i in range(len(X))], size_regression=[i for i in range(len(lineal_X))])

if (__name__=="__main__"):
    app.run(debug=True)