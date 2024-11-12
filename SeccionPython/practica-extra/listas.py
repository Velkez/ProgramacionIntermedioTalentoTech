# Lista de Estudiantes: Crea una lista con los nombres de cinco estudiantes. 
# Añade un nuevo estudiante al final de la lista, elimina el segundo estudiante 
# y reemplaza el tercer nombre con otro diferente.

def listEstudiantes():
    print ("Vamos a digitar algunos nombres de estudiantes.\n")
    estudiantes = []
    for i in range(5):
        estudiante = input(f"Digite el nombre del estudiante numero {i+1}: ")
        estudiantes.append(estudiante)
    print(f"\nLa lista de estudiantes quedó de la siguiente manera: \n{estudiantes}")
    return estudiantes
    
def addEstudiante(lista):
    estudiante = input("\nDigité el nombre del estudiante a agregar: ")
    lista.append(estudiante)
    print (f"\nLa nueva lista de estudiantes quedó de la siguiente manera: \n{lista}")
    return lista

def delEstudiante(lista, posicion = 1):
    lista.pop(posicion)
    print(f"\nSe ha eliminado el segundo estudiante. \nAhora la nueva lista quedó de la siguiente manera: \n{lista}")
    return lista
    
def updateEstudiantes(lista, posicion = 2):
    print ("\nEl tercer estudiante sera remplazado por el siguiente nombre.")
    estudiante = input("Digite el nombre: ")
    lista[posicion] = estudiante
    print (f"\nEl tercer estudiante fue remplazado por {estudiante}. \nLa lista de estudiantes quedó de la siguiente manera: \n{lista}")
    return lista

def main():
    lista = listEstudiantes()
    lista = addEstudiante(lista)
    lista = delEstudiante(lista)
    lista = updateEstudiantes(lista)
    
if __name__ == "__main__":
    main()