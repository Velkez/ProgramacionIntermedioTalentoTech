# Localiza el error en el siguiente bloque de código. Crea una excepción para evitar 
# que el programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:

def recuperar_elemento():
    lista = [1, 2, 3, 4, 5]
    print (f"Tenemos la siguiente lista: \n{lista}")


    while True:
        try:
            valor = int(input("\nIngrese el indice del valor que desea optener de la lista: "))
            lista[valor]
            print(f"\nEl valor que se solicito es {lista[valor]}")
        except IndexError:
            print ("Se esta tratando de recuperar un elemento de la lista innexistente.")
            print ("Porfavor, cambie el indice del elemento al que desea acceder")
        pregunta = input("\nDesea continuar con el programa? [Y/n]\n")
        if pregunta == "n" or pregunta == "N":
            break
        
# if __name__ == "__main__":
#     recuperar_elemento()

# Realiza una función llamada agregar_una_vez(lista, el) que reciba una lista y un elemento. 
# La función debe añadir el elemento al final de la lista con la condición de no repetir 
# ningún elemento. Además si este elemento ya se encuentra en la lista se debe invocar un 
# error de tipo ValueError que debes capturar y mostrar este mensaje en su lugar:
# Error: Imposible añadir elementos duplicados => [elemento].

def agregar_una_vez(lista, elemento):
    if elemento in lista:
        raise ValueError(f"Error: Imposible añadir elementos duplicados => {elemento} esta en {lista}")
    else:
        print (f"Se agregara el siguiente elemento a la lista: {elemento}")
        lista.append(elemento)
    return lista
        
def main():
    lista = [1,2,3,4,5,6]
    print(f"Tenemos la siguiente lista: \n{lista}")
    while True:
        try:
            elemento = int(input("\nDigite el elemento nuevo a añadir: "))
            lista = agregar_una_vez(lista, elemento)
            print (f"\nLa lista quedo de la siguiente manera: \n{lista}")
        except ValueError as e:
            print(e)
        pregunta = input("\nDesea continuar con el programa? [Y/n]\n")
        if pregunta == "n" or pregunta == "N":
            break
    
# if __name__ == "__main__":
#     main()


# REALIZAR UN PROGRAMA DONDE SE MUESTRE LAS NOTAS DE LOS ESTUDIANTES, DE MATEMATICAS, FISICA Y QUIMICA. 
# EL PROGRAMA DEBE MOSTRAR EN UNA LISTA LAS NOTAS PROMEDIOS DE LAS MATERIAS. SI LA NOTA ES INFERIOR A 3, 
# DEBE MOSTRAR UN MENSAJE DE QUE MATERIA VA PERDIENDO, SI POR ERROR EL USUARIO INGRESA UNA NOTA MAYOR DE 
# 5 O NEGATIVA, EVITAR EL ERROR POSIBLE, Y REALICE LA SUBSANACION
import re
import copy

# Función para saber si la nota esta dentro del rango de 0 a 5. En caso de no estarlo, lanzará una excepción de error.
def rango_nota(nota):
    if nota < 0 or nota > 5:
        raise ValueError("\nLa nota esta fuera del rango ==> nota >= 0 o nota <= 5")
    else:
        return nota
    
# Función para agregar las notas del estudiante para la materia digitada. Este muestra formateado las notas digitadas y el promedio de la materia.
def generar_notas(estudiante, materia,):
    try: 
        print (f"\nDigite las notas del estudiante {estudiante} para la materia de {materia}.")
        nota_1 = rango_nota(float(input("Nota 1 (20%): ")))
        nota_2 = rango_nota(float(input("Nota 2 (20%): ")))
        nota_3 = rango_nota(float(input("Nota 3 (20%): ")))
        parcial = rango_nota(float(input("Parcial (40%): ")))
        
        promedio = ((((nota_1 + nota_2 + nota_3) / 3) * 0.6) + (parcial * 0.4)) / 1
        # notas[materia] = round(promedio, 1)
        
        print (f"\nSe agregaron con exito las notas de {materia} del estudiante {estudiante}.")
        print (f"""Las notas son las siguientes: 
               Nota 1 (20%) |  Nota 2 (20%) |  Nota 3 (20%) | Parcial (40%)
               -------------+---------------+---------------+--------------
                    {round(nota_1, 1)}     |      {round(nota_2, 1)}      |      {round(nota_3, 1)}      |     {round(parcial, 1)} 
               
        Donde el promedio de la materia es: {round(promedio, 1)}
        """)
    except ValueError as e:
        print (e)
    
    return round(promedio, 1)
        
# Fución para agregar un estudiante dentro de una lista de estudiantes. Este crea la lista y almacena el nombre del estudiante dentro de esta.
def agregar_estudiantes():
    expresion = r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$"
    estudiante = input("\nNombre del estudiante a agregar: ")
    
    if re.match(expresion, estudiante):
        print (f"\nEl estudiante {estudiante} fue agregado con exito.")
    else:
        raise ValueError("Nombre no valido. Este no debe contener signos ni numeros.")
    
    return estudiante

# Función para asignar las calificaciones a cada estudiante.
def calificar_estudiante(materias, estudiante, notas={}):
    nota = 0.0
    nota_base = {"matematicas" : nota, "fisica": nota, "quimica": nota}
    expresion = r"^[sSnN]?$"
    
    while True:
        print ("\nTenemos el siguiente listado de materias: ")
        print ("\n".join(f"-. {nombre}" for i, nombre in enumerate(materias)))
        
        materia = input ("\n¿Qué materia desea calificar?: ")
        materia = materia.lower()
        
        if estudiante not in notas:
            notas[estudiante] = copy.deepcopy(nota_base)
        
        nota = generar_notas(estudiante, materia)
        
        if materia in notas[estudiante]:
            notas[estudiante][materia] = nota
        else:
            raise ValueError(f"\n'{materia}' no se encuentra registrado. Por favor, digite alguna materia del listado.")
        
        print (f"\nLas notas van de la siguiente manera: \n{notas}")
        
        pregunta = input ("\n¿Desea calificar otra materia? [S/n]:")
        if re.match(expresion, pregunta) and re.match(r"^[nN]+$", pregunta):
            break
        
    return notas

def main():
    expresion = r"^[sSnN]?$"
    materias = ["matematicas", "fisica", "quimica"]
    while True:
        try:
            respuesta = input ("\n¿Desea agregar un nuevo estudiante? [S/n]: ")
            if re.match(expresion, respuesta):
                if respuesta == "s" or respuesta == "S" or respuesta == "":
                    estudiante = agregar_estudiantes()
                    calificar_estudiante(materias, estudiante)
                else:
                    break
            else:
                raise ValueError(f"\n'{respuesta}' no es una respuesta valida.")
        except ValueError as e:
            print (e)

if __name__ == "__main__":
    main()