
#### DIVISAS ####
# monedas = {
#     "Euro": "€",
#     "Dolar": "$",
#     "Yen": "¥"
# }

# while True:
#     divisa = input("Ingrese la divisa: ")
#     if divisa in monedas:
#         print(f"{divisa}: {monedas[divisa]}")
#         break
#     else:
#         print("La divisa no encontrada.")

# import datetime
   
#### FECHAS #### 
# def set_fecha():
#     mesesDic = {
#         "01":'Enero',
#         "02":'Febrero',
#         "03":'Marzo',
#         "04":'Abril',
#         "05":'Mayo',
#         "06":'Junio',
#         "07":'Julio',
#         "08":'Agosto',
#         "09":'Septiembre',
#         "10":'Octubre',
#         "11":'Noviembre',
#         "12":'Diciembre'
#     }
#     while True:
#         fecha = input("Ingrese la fecha en el siguiente formato: dd/mm/aaaa.")
#         try:
#             validador = datetime.datetime.strptime(fecha, "%d/%m/%Y").date()
#         except ValueError:
#             print("La fecha no esta en su formato indicado.")
#         else:
#             dia,mes,anio = fecha.split("/")
#             print(f"{dia} de {mesesDic[mes]} de {anio}")
#             break

# if __name__ == "__main__":
#     set_fecha() 

#### TRADUCTOR ####
import re

def agregar_traduccion():
    patron = r'^\w+:\w+$'
    diccionario = {}
    while True:
        traduccion = input("\nIntroduzca el termino con el siguiente formato <Español>:<Ingles>.\n  Si desea terminar el diccionario, digite exit: ")
        if traduccion == "exit":
            break
        else:
            if re.match(patron, traduccion):
                español,ingles = traduccion.split(":")
                diccionario[español] = ingles
            else:
                print("\nFormato no válido.")
    
    return diccionario

def traduccion(diccionario):
    frase = input("\nintroduzca su frase a traducir: ")
    pre_traduccion = frase.split(" ")
    for i, palabra in enumerate(pre_traduccion):
        pre_traduccion[i] = diccionario.get(palabra, palabra)
    traduccion = " ".join(pre_traduccion)
    return traduccion
    

def main():
    diccionario = agregar_traduccion()
    if not diccionario:
        print("El diccionario está vacío")
    else:
        print(f"\n el diccionario quedo de la siguiente forma: \n{diccionario}")
        traduccion_ingles = traduccion(diccionario)
        print(f"\nLa traducción seria: \n{traduccion_ingles}")
    
if __name__ == "__main__":
    main() 