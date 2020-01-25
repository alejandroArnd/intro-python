import csv

with open('alumnos.csv', mode='r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=';')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {",".join(row)}')
            line_count += 1
        else:
          line_count += 1
          print(row[0]+" "+row[1]+" years old, profession "+row[2])
    print(f'Processed {line_count} lines.')