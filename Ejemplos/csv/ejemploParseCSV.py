import csv

with open('alumnos.csv', mode='r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=';')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Los nombres de las columnas son {",".join(row)}')
            line_count += 1
        else:
          line_count += 1
          print(row[0]+" "+row[1]+" años, profesion:  "+row[2])
    print(f'Procesadas {line_count} lineas.')