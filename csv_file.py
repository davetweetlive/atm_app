import csv
from csv import reader, writer

def read_csv_file(type):
    with open('FILES/record.csv') as csv_file:
        csv_reader = reader(csv_file)
        # print(list(csv_reader[1][2]))
        for row in list(csv_reader):
            print(row[2])
            # if row[2] is type:
            #     print(row)
            #     print(f'{row[0]} \t\t {row[1]} \t {row[2]} \t\t {row[3]}')
            # elif row[2] == type: 
            #     print(f'{row[0]} \t\t {row[1]} \t {row[2]} \t\t {row[3]}')

read_csv_file('Withdraw')

def update_csv_file(date_time, ammount, type_of_transection, total_left):
    with open('FILES/record.csv', 'a') as csv_file:
        csv_writer = writer(csv_file)
        csv_writer.writerow([date_time, ammount, type_of_transection, total_left])

def read_global_variable():
    pass

def update_global_variable():
    pass
