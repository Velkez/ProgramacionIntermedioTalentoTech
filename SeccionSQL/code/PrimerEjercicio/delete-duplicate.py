import csv
import sqlite3

nombrecsv = 'ejemploDB(17_OCT_24)'
formated_nombrecsv = f'{nombrecsv}_utf8.csv'
new_nombrecsv = f'{nombrecsv}_clean.csv'
database = 'clientes.db'
create_table = '''
CREATE TABLE IF NOT EXISTS clientes (
    cliente TEXT,
    cc_nit TEXT PRIMARY KEY,
    telefono TEXT,
    celular TEXT,
    direccion TEXT,
    ciudad TEXT,
    edad INTEGER,
    correo TEXT,
    direccion_envio TEXT
)
'''
insert_query = '''
        INSERT OR IGNORE INTO clientes (cliente, cc_nit, telefono, celular, direccion, ciudad, edad, correo, direccion_envio)
        VALUES (:CLIENTE, :CC_NIT, :TELEFONO, :CELULAR, :DIRECCION, :CIUDAD, :EDAD, :CORREO, :DIRECCION_ENVIO)
        '''

# # CONVERTIR A FORMATO UTF8
# # Leer el archivo original (suponiendo que está en una codificación diferente)
# with open(f'{nombrecsv}.csv', 'r', encoding='ISO-8859-1') as infile, open(formated_nombrecsv, 'w', newline='', encoding='utf-8') as outfile:
#     reader = csv.reader(infile)
#     writer = csv.writer(outfile)
    
#     # Escribir las filas en el nuevo archivo con codificación UTF-8
#     for row in reader:
#         writer.writerow(row)

# print("documento formateado a utf8\n")

# ELIMINAR LLAVES PRIMARIAS REPETIDAS
# Abrir el archivo CSV original y un archivo CSV temporal para guardar los datos sin duplicados
with open(formated_nombrecsv, 'r') as infile, open(new_nombrecsv, 'w', newline='') as outfile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    
    writer.writeheader()
    seen = set()  # Para almacenar los valores de cc_nit ya procesados
    for row in reader:
        cc_nit = row['CC_NIT']
        if cc_nit not in seen:
            writer.writerow(row)
            seen.add(cc_nit)

print(f"Duplicados eliminados. Nuevo archivo: {new_nombrecsv}")

# ASEGURARSE DE QUE LAS LLAVES PRIMARIAS NO ESTEN DUPLICADAS Y EXPORTAR CVS A LA BASE DE DATOS
# Conectar a la base de datos
conn = sqlite3.connect(database)
cursor = conn.cursor()

# Crear la tabla si no existe
cursor.execute(create_table)

# Leer el archivo CSV y insertar datos, ignorando duplicados
with open(new_nombrecsv, 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        cursor.execute(insert_query, row)

# Confirmar y cerrar la conexión
print(f"Documento {new_nombrecsv} importado a la base de datos")
conn.commit()
conn.close()