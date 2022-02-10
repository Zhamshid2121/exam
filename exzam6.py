import pandas as pandasCSV
import csv
from csv import writer



# Создаем класс для работы с csv
class CvsFile:

    def __init__(self, file):
        self.file = file
    # Сортировка по 1 полю
    def sort_file(self):
        csvData = pandasCSV.read_csv("CsvFile.csv")
        csvData.sort_values(["Wazza"],
                            axis=0,
                            ascending=[False],
                            inplace=True)

    #Добавление строки
    def add_file(self):
        #Сначала открываем файл CSV, обозначаем как 'a', а затем file object
        with open('CsvFile.csv', 'a', newline='') as f_object:
            #Используем writer и даем ему переменную
            writer_object = writer(f_object)
           #Добавляем whiterow
            writer_object.writerow('L')
           #Закрываем затем его
            f_object.close()

    def update_file(self):
        pass

    def correct_file(self):
        # Открываем файл
        with open('CsvFile.csv', 'w') as csv_object:
            #
            writer = csv.writer(csv_object, delimiter=',', quotechar='"')

            # Открываем файл
            with open('tmpEmployeeDatabase.csv', 'r') as csvFile:
                # Читаем содержимое в файле
                reader = csv.reader(csvFile, delimiter=',', quotechar='"')

                # и затем пробегаемся с помощью цикла for
                for row in reader:
                    row[0] = row[0].title()
                    writer.writerow(row)

    def search_file(self):
        pass


a = CvsFile


import csv
import operator


class CsvWork:

    def __init__(self, data):
        self.data = data

    def sort_one(self):

        with open('dict.csv') as f:
            csv_reader = csv.reader(f, delimiter=';')
            print(sorted(csv_reader, key=operator.itemgetter(1)))

    def add_row_csv(self):
        with open('dict.csv', 'a', newline='') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow((self.data['first_name'], self.data['last_name'], self.data['age'], self.data['gender'],
                             self.data['hobby'], self.data['job']))
            f.close()

    def update_line(self):

        row_num = 1
        new_value = 'Replaced Line'

        with open('dict.csv', 'r') as f:
            csv_reader = csv.reader(f, delimiter=';')
            lines = []

            for current_line in csv_reader:
                if csv_reader.line_num == row_num:
                    current_line = new_value
                lines.append(current_line)

        with open('dict.csv', 'w', newline='') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerows(lines)

    def edit_line(self):
        line_to_editing = []
        with open('dict.csv') as f:
            csv_reader = csv.reader(f, delimiter=';')
            for row in csv_reader:
                line_to_editing.append(row)
        print(line_to_editing)


jason = {'first_name': 'Jason', 'last_name': 'Houston', 'age': 29, 'gender': 'male', 'hobby': 'video games',
         'job': 'QA'}
alice = {'first_name': 'Alice', 'last_name': 'Cooper', 'age': 21, 'gender': 'female', 'hobby': 'sport',
         'job': 'software engineer'}
almaz = {'first_name': 'Almaz', 'last_name': 'Mokoeev', 'age': 45, 'gender': 'male', 'hobby': 'sport',
         'job': 'software engineer'}

work = CsvWork(jason)
work1 = CsvWork(alice)
work.add_row_csv()
work1.add_row_csv()
work.edit_line()
work.sort_one()
work2 = CsvWork(almaz)
work2.update_line()