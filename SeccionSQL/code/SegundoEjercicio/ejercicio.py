import sqlite3

conn = sqlite3.connect('ejercicioDB')

cursor =conn.cursor()
cursor.execute('''create table usuarios(
    nombre varchar(20),
    edad int(3),
    direccion varchar(50),
    telefono varchar(10)
)''')

insert_data = cursor.execute("insert into usuarios values('Velkez', 23, 'Crr 15 #6-39, Sahagún', '3115530127')")

data_usuarios =[
    ("Carlos", 25, "Calle 45 #23-56, Bogotá", '3104567890'),
    ("María", 35, "Carrera 12 #34-78, Medellín", '3205678912'),
    ("Andrés", 40, "Avenida 68 #10-25, Cali", '3006789123'),
    ("Sofía", 28, "Calle 8 #22-15, Barranquilla", '3127890134'),
    ("Camilo", 50, "Carrera 15 #7-89, Bucaramanga", '3158901245'),
    ("Luisa", 30, "Avenida Bolívar #45-67, Cartagena", '3019012356'),
    ("Esteban", 45, "Calle 93 #12-45, Bogotá", '3160123456'),
    ("Ana", 20, "Carrera 1 #3-15, Popayán", '3041234567'),
    ("Julián", 32, "Carrera 25 #18-45, Bogotá", '3172345678'),
    ("Laura", 29, "Avenida El Poblado #14-88, Medellín", '3183456789'),
    ("Manuel", 50, "Calle 10 #5-23, Cali", '3114567890'),
    ("Daniela", 22, "Carrera 7 #20-12, Pereira", '3195678901'),
    ("Felipe", 36, "Avenida Santander #45-67, Manizales", '3226789012'),
    ("Paula", 27, "Calle 22 #8-90, Cartagena", '3137890123'),
    ("Oscar", 41, "Carrera 9 #30-45, Armenia", '3148901234'),
    ("Natalia", 26, "Avenida Las Palmas #50-10, Medellín", '3009012345'),
    ("Sebastián", 38, "Calle 15 #25-40, Villavicencio", '3200123456'),
    ("Camila", 34, "Carrera 3 #12-55, Pasto", '3011234567'),
    ("Diego", 47, "Avenida Boyacá #32-76, Bogotá", '3042345678'),
    ("Isabella", 19, "Calle 50 #10-20, Bucaramanga", '3153456789'),
]

cursor.executemany('insert into usuarios values(?,?,?,?)',data_usuarios)

conn.commit()

consulta = 'select * from usuarios;'
clientes = cursor.execute(consulta)

tabla_consulta = clientes.fetchall()
for fila in tabla_consulta:
    print(fila)

conn.close();