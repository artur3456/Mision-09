#Autor: Arturo Márquez Olivar. A01376086.
#Completa las funciones requerias en la misión 9.


#De una lista, revisa si sus datos son pares y los que sí los agrega a una nueva lista y la regresa.
def extraerPares(lista):
    listaPar = []
    for par in lista:
        if par!= 0:
            if par%2 == 0:
                listaPar.append(par)
    return listaPar


#Recibe una lista y si un dato es mayor que el previo, lo regresa dentro de una nueva lista.
def extraerMayoresPrevio(lista):
    listaMayores = []
    for k in range(len(lista)-1):
        if lista[k] < lista[k+1]:
            listaMayores.append(lista[k+1])
    return listaMayores


#Regresa una lista con los valores pares cambiados de lugar, sin modificar la lista original.
def intercambiarParejas(lista):
    copiaLista = []
    for dato in lista:
        copiaLista.append(dato)

    for dato in range(len(copiaLista)-1):
        copiaLista[dato] = copiaLista[dato+1]
        copiaLista[dato+1] = copiaLista[dato]
    return copiaLista


#Recibe una lista e intercambia el mayor y menor que está dentro de esa lista
def intercambiarMM(lista):
    if len(lista) > 0:
        mayor = max(lista)
        menor = min(lista)
        for k in range(len(lista)):
            if lista[k] == menor:
                lista[k] = mayor
            elif lista[k] == mayor:
                lista[k] = menor
            else:
                pass
    return lista


#Saca el promedio entero de los valores de una lista sin tomar al mayor y menor de la lista. Sin modificar la lista.
def promediarCentro(lista):
    acumulador = 0
    contador = 0
    if len(lista) > 0:
        mayor = max(lista)
        menor = min(lista)
        for dato in lista:
            if dato != mayor and dato != menor:
                acumulador += dato
                contador += 1
        if contador > 0:
            promedio = acumulador//contador
            return promedio
        return 0
    return 0


#Recibe una lista de números y regresa una dupla con la media y la desviación estándar.
def calcularEstadistica(lista):
    if len(lista) > 0:
        n = len(lista)
        Xi = sum(lista)
        mean = Xi / n
        x = 0
        for k in lista:
            x += (k - mean)**2
        deviation = (x / (n - 1))**.5
        return (mean, deviation)
    return (0, 0)


#Recibe una lista y hace la suma de todos sus valores siempre y cuando no estén al lado del número 13.
def calcularSuma(lista):
    if len(lista) > 0:
        suma = 0
        for dato in range(len(lista)):
            if [dato] == 13:
                del(lista[dato+1])
                del(lista[dato-1])
                del(lista[dato])
            suma += lista[dato]
        return suma
    return lista


#Función principal, ejecuta las funciones e imprime los resultados.
def main():
    print("Problema 1. Regresa una lista con los valores pares de la lista original.")
    lista1 = [1, 2, 3, 2, 4, 60, 5, 8, 3, 22, 44, 55]
    paresLista1= extraerPares(lista1)
    print("Con la lista", lista1,"regresa,", paresLista1)
    lista2 = [5, 7, 3]
    paresLista2 = extraerPares(lista2)
    print("Con la lista", lista2, "regresa,", paresLista2)
    lista3 = []
    paresLista3 = extraerPares(lista3)
    print("Con la lista", lista3, "regresa,", paresLista3)
    print("")


    print("Problema 2. Regresa una lista con los valores que son mayores al previo de la lista original")
    #lista1 = [1, 2, 3, 2, 4, 60, 5, 8, 3, 22, 44, 55]
    mayoresLista1 = extraerMayoresPrevio(lista1)
    print("Con la lista", lista1, "regresa,", mayoresLista1)
    lista4 = [5, 4, 3, 2]
    mayoresLista4 = extraerMayoresPrevio(lista4)
    print("Con la lista", lista4, "regresa,", mayoresLista4)
    lista5 = []
    mayoresLista5 = extraerMayoresPrevio(lista5)
    print("Con la lista", lista5, "regresa,", mayoresLista5)
    print("")


    print("Problema 3. Regresa una lista con los valores PARES cambiados de lugar, sin modificar la lista original.")
    lista1 = [1, 2, 3, 2, 4, 60, 5, 8, 3, 22, 44, 55]
    modificadosLista1 = intercambiarParejas(lista1)
    print("Con la lista", lista1, "regresa,", modificadosLista1)
    lista6 = [1, 2, 3]
    modificadosLista2 = intercambiarParejas(lista6)
    print("Con la lista", lista6, "regresa,", modificadosLista2)
    lista7 = [7]
    modificadosLista3 = intercambiarParejas(lista7)
    print("Con la lista", lista7, "regresa,", modificadosLista3)
    lista8 = []
    modificadosLista4 = intercambiarParejas(lista8)
    print("Con la lista", lista8, "regresa,", modificadosLista4)
    print("")


    print("Problema 4. Recibe una lista e intercambia el mayor y menor que está dentro de esa lista, modificando a la lista original.")
    lista9 = [5, 9, 3, 22, 19, 31, 10, 7]
    listaCambiada1 = intercambiarMM(lista9)
    print("Con la lista [5, 9, 3, 22, 19, 31, 10, 7], regresa,",listaCambiada1)
    lista10 = [1, 2, 3]
    listaCambiada2 = intercambiarMM(lista10)
    print("Con la lista [1, 2, 3], regresa,", listaCambiada2)
    lista11 = []
    listaCambiada3 = intercambiarMM(lista11)
    print("Con la lista [], regresa,", listaCambiada3)
    print("")


    print("Problema 5. Saca el promedio entero de los valores de una lista sin tomar al mayor y menor de la lista. Sin modificar la lista.")
    lista12 = [70, 80, 90]
    promedio1 = promediarCentro(lista12)
    print("Con la lista", lista12, "regresa,", promedio1)
    lista13 = [95, 21, 73, 24, 15, 69, 71, 80, 49, 100, 85]
    promedio2 = promediarCentro(lista13)
    print("Con la lista", lista13, "regresa,", promedio2)
    lista14 = [20, 55, 30, 5, 55, 5]
    promedio3 = promediarCentro(lista14)
    print("Con la lista", lista14, "regresa,", promedio3)
    lista15 = [5, 9, 1, 8]
    promedio4 = promediarCentro(lista15)
    print("Con la lista", lista15, "regresa,", promedio4)
    lista16 = [5, 8]
    promedio5 = promediarCentro(lista16)
    print("Con la lista", lista16, "regresa,", promedio5)
    lista17 = [1]
    promedio6 = promediarCentro(lista17)
    print("Con la lista", lista17, "regresa,", promedio6)
    lista18 = []
    promedio7 = promediarCentro(lista18)
    print("Con la lista", lista18, "regresa,", promedio7)
    print("")


    print("Problema 6. Recibe una lista de números y regresa una dupla con la media y la desviación estándar.")
    lista19 = [1, 2, 3, 4, 5, 6]
    estadistica = calcularEstadistica(lista19)
    print("Con la lista", lista19, "regresa,", estadistica)
    lista20 = [95, 21, 73, 24, 15, 69, 71, 80, 49, 100, 85]
    estadistica2 = calcularEstadistica(lista20)
    print("Con la lista", lista20, "regresa,", estadistica2)
    lista21 = []
    estadistica3 = calcularEstadistica(lista21)
    print("Con la lista", lista21, "regresa,", estadistica3)
    print("")


    print("Problema EXTRA. Recibe una lista y hace la suma de todos sus valores siempre y cuando no estén al lado del número 13.")
    lista22 = [1, 2, 3, 4, 5, 6]
    suma = calcularSuma(lista22)
    print("Con la lista", lista22, "regresa,", suma)
    lista23 = [5, 2, 13, 4, 1, 6, 1, 8, 4, 1, 5]
    suma2 = calcularSuma(lista23)
    print("Con la lista", lista23, "regresa,", suma2)
    lista24 = [5, 2, 13, 4, 1, 6, 1, 8, 4, 13, 1]
    suma3 = calcularSuma(lista24)
    print("Con la lista", lista24, "regresa,", suma3)
    lista25 = [13, 49]
    suma4 = calcularSuma(lista25)
    print("Con la lista", lista25, "regresa,", suma4)
    lista26 = []
    suma5 = calcularSuma(lista26)
    print("Con la lista", lista26, "regresa,", suma5)
    print("")


#Llamada a la función principal.
main()