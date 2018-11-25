import csv
from csv import reader

def read_csv_file():
    with open('record.csv') as csv_file:
        csv_reader = reader(csv_file)
        for row in csv_reader:
            print(f'{row[0]} \t\t {row[1]} \t {row[2]} \t\t {row[3]}')

read_csv_file()
def update_csv():
    pass