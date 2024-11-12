def crear_lista(numero):
    if numero < 1:
        print("Lo sentimos, no se puede crear la lista.")
        return[]
    else:
        lista=[]
        for n in range(numero):
            palabra = input("Ingrese palabra: ")
            lista += [palabra]
        print(f"se creo la siguiente lista: \n {lista}")
        return lista


def buscar(lista, palabra):
    if palabra == "":
        print("No ingreso una palabra")
        return None
    else:
        for i, elemento in enumerate(lista):
            if palabra == elemento:
                print(f"La palabra {palabra} se encuentra en la posición {i} de la lista")
                return i
        print(f"La palabra '{palabra}' no se encuentra en la lista.")
        return None
        
                
def eliminar(lista, palabra):
    posicion = int(buscar(lista, palabra))
    if posicion is not None:
        print(f"el elemento a eliminar es: {posicion}")
        print(f"y la lista es: {lista}")
        lista.pop(posicion)
        print(f"la palabra {palabra} fue eliminada con exito")
    else:
        print("No se pudo eliminar la palabra")
        
    print(f"La lista quedo de la siguiente manera: \n {lista}")

        
def main():
    numero = int(input("¿Cuantas palabras tiene la lista? \n"))
    lista = crear_lista(numero)
    palabra = input("Digite la palabra a eliminar: \n")
    buscar(lista, palabra)
    eliminar(lista, palabra)
    
        
if __name__ == "__main__":
    main() 