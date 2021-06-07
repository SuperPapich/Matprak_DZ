import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def get_data():
    """ №1 Загруза данных"""
    data = pd.read_csv('data.csv')
    # Берем первые 10 значений
    first_ten = data.head(10)
    # Берем последние 10 значений
    last_ten = data.tail(10)

    # print(first_ten)
    # print(last_ten)

    # Увеличиваем максимальное количество колонок
    pd.options.display.max_columns = 30

    first_ten_increased = data.head(10)
    last_ten_increased = data.tail(10)

    # print(first_ten_increased)
    # print(last_ten_increased)

    # Выведем размер датасета
    data_shape = data.shape
    # print(data_shape)

    # Выведем информацию о датасете
    #data.info()

    return data


def easy_stat(data):
    """ №2 Простая статистика"""
    # Количество элементов
    count_data = data.count()
    # print(count_data)
    # Уникальные значения
    unique_data = data.nunique()
    # print(unique_data)
    # Базовая статистика
    desribe_data = data.describe()
    # print(desribe_data)


def hard_stat(date):
    """ №3 Не такая уж простая статистика"""
    # Матрица корреляции
    correlation = data.corr()

    # print(correlation)
    correlation_shape = correlation.shape
    # print(correlation_shape)

    # Удаляем колонку с наибольшей корреляцией с ценой
    highest_corr = correlation.drop("price", axis=0)["price"].idxmax()
    return correlation


def clear_data(data):
    """ №4 Очистка данных"""
    # Дропамем колонку зипкод
    data.drop("zipcode", axis=1, inplace=True)
    data.set_index("id", inplace=True)
    # print(data.head(10))
    # print(data.shape)


def basic_work_with_date(data):
    """ №5 Базовая обработка дат"""
    # Конвертируем дату в удобный формат
    data.date = pd.to_datetime(data.date)
    # Вытаскиваем из даты нужные части
    data["year"] = data.date.dt.year
    data["month"] = data.date.dt.month
    data["day"] = data.date.dt.day
    data["weekday"] = data.date.dt.weekday
    # Дропаем изначальну колонку даты
    data.drop("date", axis=1, inplace=True)

    # print(data.head(10))
    # print(data.shape)


def build_histogram(data):
    """ №6 Построение гистограммы"""
    # Строим гистограму
    plt.hist(data.price, bins=100)
    plt.title("Price distribution")
    plt.xlabel("Price")
    plt.ylabel("NUmber of flats")
    # plt.show()


def build_poin_diagram(correlation):
    """ №7 Построение точечной диаграммы """
    # print(correlation.price.sort_values())
    x = correlation.price
    y = correlation.sqft_living
    colors = np.random.rand(20)
    plt.rcParams["axes.facecolor"] = "#CBF5EF"
    plt.scatter(x, y, c=colors, alpha=1, marker="1")
    plt.title("Price correlation")
    plt.xlabel("Price")
    plt.ylabel("Sqft_living")
    #plt.show()


def dop_clear_data(data):
    """ №8 Дополнительная очистка данных """
    data.price.quantile(0.99)
    data = data[data.price < data.price.quantile(0.99)]
    # print(data.shape)


def more_graphics(data, correlation):
    """ №9 Построить доп. графики """
    #sns.barplot(x="weekday", y="price", data=data, color='blue')
    #plt.show()

    #sns.boxplot(x="view", y="price", data=data, hue="condition")
    #plt.show()

    sns.jointplot(x="price", y="weekday", data=data, kind="kde")
    plt.show()


def learning(data):
    """ №10 машинное обучение"""
    y = data["price"]
    x = data.drop("price", axis=1)



if __name__ == "__main__":
    data = get_data()
    easy_stat(data)
    correlation = hard_stat(data)
    clear_data(data)
    basic_work_with_date(data)
    #build_histogram(data)
    #build_poin_diagram(correlation)
    dop_clear_data(data)
    more_graphics(data, correlation)
    learning(data)
