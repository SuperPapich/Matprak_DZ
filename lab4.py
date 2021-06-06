import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


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


def easy_stat(data) -> None:
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


if __name__ == "__main__":
    data = get_data()
    easy_stat(data)
    correlation = hard_stat(data)
