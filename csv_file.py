import csv
from csv import reader, writer

def read_csv_file(type):
    with open('record.csv') as csv_file:
        csv_reader = reader(csv_file)
        next(csv_reader)
        for row in csv_reader:
            print(f'{row[0]} \t\t {row[1]} \t {row[2]} \t\t {row[3]}')
        

def update_csv_file(date_time, ammount, type_of_transection, total_left):
    with open('record.csv', 'w') as csv_file:
        csv_writer = writer(csv_file)
        csv_writer.writerow([date_time, ammount, type_of_transection, total_left])