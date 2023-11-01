from flask import Flask, render_template, request
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
import base64
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

#  Зависимость цены от категории
dictionary_mean = {
    774.667474: 'Beauty',
    10515.385267: 'Electronics',
    698.287078: 'Fashion',
    538.170048: 'Groceries',
    1181.128744: 'Home & Kitchen',
    9395.857143: 'Jewellery'
}

dictionary_count = {
    60329: 'Home & Kitchen',
    46043: 'Groceries',
    26087: 'Fashion',
    19018: 'Electronics',
    10733: 'Beauty',
    70: 'Jewellery'
}

data = pd.read_csv('csv_files/csv_encoded.csv', sep=',')
data.dropna(inplace=True)

# print(data['category'].value_counts())

x = data['category_count_price']
y = data['price']

xy = x * y
xx = x * x
sumX = x.sum()
sumY = y.sum()
sumXY = xy.sum()
sumXX = xx.sum()
n = data.shape[0]
b1 = (sumXY - (sumY * sumX) / n) / (sumXX - sumX * sumX / n)
b0 = (sumY - b1 * sumX) / n


def encoding():
    df = pd.read_csv('csv_files/jio_mart_items.csv', sep=',')
    df.dropna(inplace=True)

    df['category_mean_price'] = df['category'].map(df.groupby('category')['price'].mean().round())
    df['category_count_price'] = df['category_mean_price']

    df['category_count_price'].where(~(df['category'] == 'Home & Kitchen'), other=60329, inplace=True)
    df['category_count_price'].where(~(df['category'] == 'Jewellery'), other=70, inplace=True)
    df['category_count_price'].where(~(df['category'] == 'Groceries'), other=46043, inplace=True)
    df['category_count_price'].where(~(df['category'] == 'Fashion'), other=26087, inplace=True)
    df['category_count_price'].where(~(df['category'] == 'Electronics'), other=19018, inplace=True)
    df['category_count_price'].where(~(df['category'] == 'Beauty'), other=10733, inplace=True)

    df.to_csv('csv_files/csv_encoded.csv', index=False)


# encoding()


def linear_regression_2():
    x_ = np.array(data['category_mean_price']).reshape((-1, 1))
    y_ = data['price']
    model = LinearRegression()
    model.fit(x_, y_)

    y_pred = model.predict([[9395.857143]])
    # y_pred = model.intercept_ + model.coef_ * x
    # print(model.intercept_)
    # print(model.coef_)
    print('predicted response:', y_pred, sep='\n')


@app.route('/')
def home():
    return render_template("lab5_home.html")


@app.route('/linear_regression', methods=['GET'])
def linear_regression():
    value = int(request.args['select_category'])
    y_pred = b0 + b1 * value
    # print('predicted response1:', y_pred, sep='\n')
    return render_template("lab5_lr.html",
                           category=dictionary_count[value],
                           price=y_pred)


@app.route('/scatter_plot', methods=['GET'])
def scatter_plot():
    plt.scatter(x.iloc[:round(n * 0.99)], y.iloc[:round(n * 0.99)], color='g')
    y_pred = b0 + b1 * x
    plt.title('99% данных')
    plt.plot(x.iloc[:round(n * 0.99)], y_pred.iloc[:round(n * 0.99)], color='b')
    # plt.savefig('./plots/99proc.png')

    # создание временного файла
    tmpfile = BytesIO()
    plt.savefig(tmpfile, format='png')
    plt.clf()
    encoded1 = base64.b64encode(tmpfile.getvalue()).decode('utf-8')  # кодирование

    plt.scatter(x.iloc[round(n * 0.99):], y.iloc[round(n * 0.99):], color='g')
    y_pred = b0 + b1 * x
    plt.title('1% данных')
    plt.plot(x.iloc[round(n * 0.99):], y_pred.iloc[round(n * 0.99):], color='b')
    # plt.savefig('./plots/1proc.png')

    # создание временного файла
    plt.savefig(tmpfile, format='png')
    plt.clf()
    encoded2 = base64.b64encode(tmpfile.getvalue()).decode('utf-8')  # кодирование
    return render_template('lab5_plot.html',
                           encoded1=encoded1,
                           encoded2=encoded2)


if __name__ == '__main__':
    app.run(debug=True, threaded=True)