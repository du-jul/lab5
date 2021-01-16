# -*- coding: utf-8 -*-

import csv
import os


class Auto:

    def __init__(self, m, n):
        self.model = m
        self.number = n

    def __getitem__(self, key):
        return self.model[key]

    def set_model(self, key, value):
        self.__setattr__(key, value)

    def get_model(self, key):
        return self.__getitem__(key)

    def set_number(self, key, value):
        self.__setattr__(key, value)

    def get_number(self, key):
        return self.__getitem__(key)


class Driveway(Auto):

    def __init__(self, i, d, m, n):
        Auto.__init__(self, m, n)
        self.id = i
        self.date_time = d

    def __setattr__(self, attr, value):
        if attr == '#':
            self.__dict__[attr] = value
        elif attr == 'model':
            self.__dict__[attr] = value
        elif attr == 'number':
            self.__dict__[attr] = value
        elif attr == 'date and time':
            self.__dict__[attr] = value
        else:
            raise AttributeError

    def __getitem__(self, key):
        b = []
        return b[self.id[key], self.__model[key], self.__number[key], self.date_time[key]]

    def set_id(self, key, value):
        self.__setattr__(key, value)

    def get_id(self, key):
        return self.__getitem__(key)

    def set_date_time(self, key, value):
        self.__setattr__(key, value)

    def get_date_time(self, key):
        return self.__getitem__(key)

    def read_csv(self):
        """
        Метод read_csv считывает данные из файла и заносит их в классы
        """
        with open("arr.csv", 'r') as arr:
            r = csv.DictReader(arr, delimiter=";")
            for i, row in enumerate(r):
                for j, item in enumerate(row):
                    if j == 0:
                        self.id.set_id(i, row["#"])
                    elif j == 1:
                        self.model.set_model(i, row["model"])
                    elif j == 2:
                        self.number.set_number(i, row["number"])
                    elif j == 3:
                        self.date_time.set_date_time(i, row["date and time"])

    def write_csv(self):
        """
        Метод write_csv записывает в файл изменённые данные
        """
        with open("arr.csv", "w") as arr:
            w = csv.DictWriter(arr,
                               delimiter=";",
                               fieldnames=["#", "model", "number", "date and time"],
                               lineterminator="\r")
            w.writeheader()
            i = 0
            while True:
                try:
                    w.writerow({
                        "#": self.id.get_id(i),
                        "model": self.model.get_model(i),
                        "number": self.number.get_number(i),
                        "date and time": self.date_time.get_date_time(i)
                    })
                    i += 1
                except KeyError:
                    break

    def rewrite_variables(self, name, key, value):
        """
        Метод rewrite_variables изменяет любое значение строки
        :param name: столбец в таблице
        :param key: номер строки
        :param value: значение
        :return:
        """
        if name == "#":
            self.id.set_id(int(key), value)
        elif name == "model":
            self.model.__set_model(int(key), value)
        elif name == "number":
            self.number.__set_number(int(key), value)
        elif name == "date and time":
            self.date_time.set_date_time(int(key), value)
        else:
            raise Exception("Нет такого поля")

    def sort_dict(self, arg):
        """
        Метод sort_dict сортирует массив и возвращает отсортированные данные обратно в сущности
        :param arg: ключ, по которому происходит сортировка
        """
        arr = []
        i = 0
        while True:
            try:
                arr.append({
                    "#": self.id.get_id(i),
                    "model": self.model.__get_model(i),
                    "number": self.number.__get_number(i),
                    "date and time": self.date_time.get_date_time(i)
                })
                i += 1
            except KeyError:
                break
        arr.sort(key=lambda item: item[arg])
        for i in range(len(arr)):
            print(arr[i])
            self.id.set_id(i, arr[i]["#"])
            self.model.__set_model(i, arr[i]["model"])
            self.number.__set_number(i, arr[i]["number"])
            self.date_time.set_date_time(i, arr[i]["date and time"])

    def print_dict(self):
        """
        Метод print_dict выводит все записи из файла в консоль
        """
        i = 0
        while True:
            try:
                print({"#": self.id.get_id(i),
                       "model": self.model.get_model(i),
                       "number": self.number.get_number(i),
                       "date and time": self.date_time.get_date_time(i)})
                i += 1
            except KeyError:
                break

    def print_some_row(self):
        """
        Метод print_some_row выводит значение по заданному критерию(вывести все записи, у которых артикул больше 2)
        """
        i = 0
        while True:
            try:
                if self.id.get_id(i) > 2:
                    print({"#": self.id.get_id(i),
                           "model": self.model.__get_model(i),
                           "number": self.number.__get_number(i),
                           "date_time": self.date_time.get_date_time(i)})
                i += 1
            except KeyError:
                break

    @staticmethod
    def count_file(path):
        """
        Статический метод count_file выполняет подсчёт файлов в выбранной директории
        :param path: путь к директории
        """
        cnt = len([name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))])
        print(cnt)




class Static:
    """
    Класс содержит статические методы
    """
    @staticmethod
    def iter_obj():
        """
        Статический метод iter_obj содержит итерируемый объект
        """
        obj = iter(["Рассчитайсь...\n","Первый\n", "Второй\n"," Третий\nРасчёт окончен...\n"])
        while True:
            try:
                print(next(obj))
            except StopIteration:
                break

    @staticmethod
    def test_generator():
        """
        Статический метод test_generator содержит генератор
        """
        for i in (i for i in range(10)):
            print(i, end=" ")
        print()





def main():
    """
    Главная функция, в которой происходит вызов остальных функций
    """

    Driveway.read_csv()
    print("Список возможностей программы:")
    print("1 - Вывести все записи")
    print("2 - Изменить какое либо значение из записи")
    print("3 - Вывод записи по критерию")
    print("4 - Сортировка по записей по ключу")
    print("5 - Запись данных в файл")
    print("6 - Подсчёт файлов в директории")
    while True:
        var = input("Введите ваш выбор: ")
        if var == "1":
            Driveway.print_dict()
        elif var == "2":
            Driveway.rewrite_variables(input("Поле: "), input("Ключ: "), input("Значение: "))
        elif var == "3":
            Driveway.print_some_row()
        elif var == "4":
            Driveway.sort_dict(input("Ключ: "))
        elif var == "5":
            Driveway.write_csv()
        elif var == "6":
            Driveway.count_file(input("Путь: "))
        else:
            print("Работа программы завершена")
            break


if __name__ == '__main__':
    main()
