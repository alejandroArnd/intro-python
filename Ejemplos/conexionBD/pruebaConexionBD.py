import datetime

import pymysql

# Conectar con base de datos
conexion = pymysql.connect(host="51.91.58.160",
                           user="alejandro",
                           passwd="choosenone",
                           database="PUJAS")
cursor = conexion.cursor()

# Recuperar registros de la tabla 'Usuarios'
registros = "SELECT TITULO FROM PRODUCTOS;"

# Mostrar registros
cursor.execute(registros)
filas = cursor.fetchall()
for fila in filas:
   print(fila)


# Prepare SQL query to INSERT a record into the database.
sql = """INSERT INTO PRODUCTOS (ID_USUARIO, REF, TITULO, DESCRIPCION, INICIO, FIN, PRECIO_SALIDA) VALUES(%s,%s,%s,%s,%s,%s,%s)"""

inicio=datetime.datetime(2020, 1, 31);
fin=datetime.datetime(2020,2,1);

args = (1000,"ASU99","ASUS TUF Gaming FX505DY-BQ024 - Portátil Gaming","Es peor que el de ruben pero bueno no hay dinero", inicio.strftime('%Y/%m/%d'), fin.strftime('%Y/%m/%d'),600)

try:
    # Execute the SQL command
    cursor.execute(sql, args)
    # Commit your changes in the database
    conexion.commit()

except Exception as e:
    print(e)
    conexion.rollback();
# Finalizar
conexion.close()