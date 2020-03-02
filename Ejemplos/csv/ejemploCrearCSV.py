import csv

with open('myCSV.csv', mode='w') as file:
    writer = csv.writer(file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    writer.writerow(['Lenguaje de programacion', 'Creado por', 'Creacion', 'Extension'])
    writer.writerow(['Python', 'Guido van Rossum', '1991', '.py'])
    writer.writerow(['Java', 'James Gosling', '1995', '.java'])
    writer.writerow(['C++', 'Bjarne Stroustrup', '1985', '.cpp'])