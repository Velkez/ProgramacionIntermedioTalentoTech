# Localiza el error en el siguiente bloque de código. Crea una excepción para evitar 
# que el programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:

# lista = [1, 2, 3, 4, 5]
# print (f"Tenemos la siguiente lista: \n{lista}")


# while True:
#     try:
#         valor = int(input("\nIngrese el indice del valor que desea optener de la lista: "))
#         lista[valor]
#         print(f"\nEl valor que se solicito es {lista[valor]}")
#     except IndexError:
#         print ("Se esta tratando de recuperar un elemento de la lista innexistente.")
#         print ("Porfavor, cambie el indice del elemento al que desea acceder")
#     pregunta = input("\nDesea continuar con el programa? [Y/n]\n")
#     if pregunta == "n" or pregunta == "N":
#         break

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
    
if __name__ == "__main__":
    main()
