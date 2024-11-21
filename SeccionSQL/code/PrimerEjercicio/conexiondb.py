import sqlite3

conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()

consulta = 'select cliente from clientes;'
clientes = cursor.execute(consulta)

tabla_consulta = clientes.fetchall()
for fila in tabla_consulta:
    print(fila)
    

conn.close()