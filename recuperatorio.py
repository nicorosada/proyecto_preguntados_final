import random

#PUNTO 1
def inicializar_matriz(cantidad_filas: int, cantidad_columnas: int) -> list:
    """
    Crea una matriz donde por parametro recibe la cantidad de filas y cantidad de columnas, 
    cada elemento se inicializa en cero.
    """
    matriz = []
    for i in range(cantidad_filas):
        fila = [0] * cantidad_columnas
        matriz = matriz + [fila]
    return matriz


def cargar_votos(matriz:list) -> None:
    """
    Solicita y carga los votos para una lista de candidatos en tres turnos distintos en una matriz haciendo sus respectivas validaciones.
    """

    for i in range(5): 
        nro_lista = int(input(f"Ingrese el número de lista para la lista {i + 1} (3 cifras): "))
        while nro_lista < 100 or nro_lista > 999:
            nro_lista = int(input("Número de lista inválido. Ingrese un número de 3 cifras: "))
        
        votos_mañana = int(input(f"Ingrese votos para la lista {nro_lista} en el turno mañana: "))
        while votos_mañana < 0:
            votos_mañana = int(input("Cantidad inválida. Ingrese votos positivos para la mañana: "))
        
        votos_tarde = int(input(f"Ingrese votos para la lista {nro_lista} en el turno tarde: "))
        while votos_tarde < 0:
            votos_tarde = int(input("Cantidad inválida. Ingrese votos positivos para la tarde: "))

        votos_noche = int(input(f"Ingrese votos para la lista {nro_lista} en el turno noche: "))
        while votos_noche < 0:
            votos_noche = int(input("Cantidad inválida. Ingrese votos positivos para la noche: "))

        
        matriz[i][0] = nro_lista
        matriz[i][1] = votos_mañana
        matriz[i][2] = votos_tarde
        matriz[i][3] = votos_noche


#PUNTO 2
def mostrar_votos(matriz:list) -> None:
    """
    Muestra los resultados de las votaciones por consola de una manera ordenada y linda 
    """
    total_votos= calcular_total_votos(matriz)
    print("\nResultados de la votación:")
    for i in range(5):
        nro_lista = matriz[i][0]
        votos_mañana = matriz[i][1]
        votos_tarde = matriz[i][2]
        votos_noche = matriz[i][3]
        total_lista = votos_mañana + votos_tarde + votos_noche
        
        if total_votos > 0:
            porcentaje = (total_lista / total_votos) * 100
        else:
            0
        print(f"Nro Lista {nro_lista} || Votos Mañana {votos_mañana} || Votos Tarde {votos_tarde} || Votos Noche {votos_noche} || Porcentaje de Votos {porcentaje:.2f}%")

#PUNTO 3
def ordenar_votos_mañana(matriz:list) -> None:
    """
    Ordena la matriz de mayor a menor por la cantidad de votos que tuvieron en el turno mañana
    """
    for i in range(4):  
        for j in range(4 - i):
            if matriz[j][1] < matriz[j + 1][1]: 
                aux = matriz[j]
                matriz[j] = matriz[j + 1]
                matriz[j + 1] = aux

#PUNTO 4
def no_te_voto_nadie(matriz:list) -> None:
    """
    Muestra las listas que tengan menos del 5% de todos los votos
    """
    bandera=False
    total_votos = calcular_total_votos(matriz)

    print("\nListas con menos del 5% de los votos:")
    for i in range(5):
        votos_lista = matriz[i][1] + matriz[i][2] + matriz[i][3]
        if votos_lista < 0.05 * total_votos:
            bandera = True
            print(f"Lista {matriz[i][0]}: {votos_lista} votos")
    
    if bandera==False:
        print("Ninguna lista tiene menos del 5% de los votos")



#PUNTO 5
def turno_mas_votado(matriz:list) -> None:
    """
    Muestra cuál fue el turno o los turnos al que más alumnos fueron a votar.
    """
    votos_mañana = 0
    votos_tarde = 0
    votos_noche = 0
    
    for i in range(len(matriz)):
        votos_mañana = votos_mañana + matriz[i][1]
        votos_tarde = votos_tarde + matriz[i][2]
        votos_noche = votos_noche + matriz[i][3]

    if votos_mañana > votos_tarde and votos_mañana > votos_noche:
        print("El turno al que más fueron a votar es: Mañana")
    elif votos_tarde > votos_mañana and votos_tarde > votos_noche:
        print("El turno al que más fueron a votar es: Tarde")
    elif votos_noche > votos_mañana and votos_noche > votos_tarde:
        print("El turno al que más fueron a votar es: Noche")
    else:
        print("Hay un empate entre los turnos:")
        if votos_mañana == votos_tarde and votos_mañana == votos_noche:
            print("- Mañana - Tarde y - Noche")
        elif votos_mañana == votos_tarde:
            print("- Mañana y - Tarde")
        elif votos_mañana == votos_noche:
            print("- Mañana y - Noche")
        elif votos_tarde == votos_noche:
            print("- Tarde y - Noche")

#PUNTO 6
def verificar_ballotage(matriz:list) -> None:
    """
    Verifica si hay segunda vuelta o no, La única
    forma de evitar la segunda vuelta es que una lista tenga más del 50% de los votos
    """
    total_votos = calcular_total_votos(matriz)

    hay_ganador = False
    for i in range(len(matriz)):
        votos_lista = matriz[i][1] + matriz[i][2] + matriz[i][3]
        porcentaje = (votos_lista / total_votos) * 100
        
        if porcentaje > 50:
            print(f"La lista {matriz[i][0]} ha ganado con el {porcentaje:.2f}% de los votos. No habrá segunda vuelta.")
            hay_ganador = True
            break

    if hay_ganador == False:
        print("Ninguna lista ha alcanzado más del 50% de los votos. Habrá segunda vuelta.")


#PUNTO 7
def calcular_total_votos(matriz: list) -> int:
    """
    Calcula el total de votos sumando los votos de todas las listas en los distintos turnos.
    """
    total_votos = 0
    for i in range(len(matriz)):
        total_votos = total_votos + matriz[i][1] + matriz[i][2] + matriz[i][3]
    return total_votos

def encontrar_listas_mas_votadas(matriz: list) -> list:
    """
    Identifica las dos listas con el mayor número de votos.
    """
    votos_lista_1 = -1
    votos_lista_2 = -1
    listas_mas_votadas = [-1, -1]  

    for i in range(len(matriz)):
        votos_lista = matriz[i][1] + matriz[i][2] + matriz[i][3]
        if votos_lista > votos_lista_1:
            votos_lista_2 = votos_lista_1
            listas_mas_votadas[1] = listas_mas_votadas[0]  
            votos_lista_1 = votos_lista
            listas_mas_votadas[0] = matriz[i][0]  
        elif votos_lista > votos_lista_2:
            votos_lista_2 = votos_lista
            listas_mas_votadas[1] = matriz[i][0]  

    return listas_mas_votadas

def cargar_votos_segunda_vuelta(segunda_vuelta: list, lista_1: int, lista_2: int) -> None:
    """
    Genera y asigna votos aleatorios a las dos listas de participantes en la segunda vuelta.
    """
    for i in range(2):
        if i == 0:
            lista_actual = lista_1
        else:
            lista_actual = lista_2
            
        print(f"\nCalculando los votos para la lista {lista_actual}")
        
        votos_mañana = random.randint(0, 100)
        votos_tarde = random.randint(0, 100)
        votos_noche = random.randint(0, 100)
        
        segunda_vuelta[i][0] = lista_actual
        segunda_vuelta[i][1] = votos_mañana
        segunda_vuelta[i][2] = votos_tarde
        segunda_vuelta[i][3] = votos_noche

def mostrar_resultado_segunda_vuelta(segunda_vuelta: list) -> None:
    """
    Calcula y muestra el resultado de la segunda vuelta de votación, incluyendo el total de votos y porcentaje para cada lista.
    """
    total_votos_2_lista_1 = segunda_vuelta[0][1] + segunda_vuelta[0][2] + segunda_vuelta[0][3]
    total_votos_2_lista_2 = segunda_vuelta[1][1] + segunda_vuelta[1][2] + segunda_vuelta[1][3]
    
    total_votos_segunda_vuelta = total_votos_2_lista_1 + total_votos_2_lista_2
    porcentaje_1 = (total_votos_2_lista_1 / total_votos_segunda_vuelta) * 100
    porcentaje_2 = (total_votos_2_lista_2 / total_votos_segunda_vuelta) * 100

    print(f"\nResultados de la segunda vuelta:")
    print(f"Lista {segunda_vuelta[0][0]}: {total_votos_2_lista_1} votos ({porcentaje_1:.2f}%)")
    print(f"Lista {segunda_vuelta[1][0]}: {total_votos_2_lista_2} votos ({porcentaje_2:.2f}%)")

    if porcentaje_1 > porcentaje_2:
        print(f"\nLa lista {segunda_vuelta[0][0]} ha ganado la segunda vuelta.")
    elif porcentaje_2 > porcentaje_1:
        print(f"\nLa lista {segunda_vuelta[1][0]} ha ganado la segunda vuelta.")
    else:
        print("\nHa ocurrido un empate en la segunda vuelta.")

def realizar_segunda_vuelta(matriz: list) -> None:
    """
    Realiza el proceso completo de la segunda vuelta, desde la identificación de las listas más votadas
    hasta el cálculo y visualización del resultado final.
    """
    total_votos = calcular_total_votos(matriz)
    
    listas_mas_votadas = encontrar_listas_mas_votadas(matriz)
    lista_1 = listas_mas_votadas[0]
    lista_2 = listas_mas_votadas[1]
    
    if lista_1 == -1 or lista_2 == -1:
        print("No hay suficientes candidatos para una segunda vuelta.")
        return

    print(f"\nLas dos listas más votadas son: Lista {lista_1} y Lista {lista_2}")
    
    segunda_vuelta = inicializar_matriz(2, 4)
    cargar_votos_segunda_vuelta(segunda_vuelta, lista_1, lista_2)
    
    mostrar_resultado_segunda_vuelta(segunda_vuelta)


def menu():
    matriz = inicializar_matriz(5, 4)
    while True:
        print("\n--- Sistema de Elecciones ---")
        print("1. Cargar Votos")
        print("2. Mostrar Votos")
        print("3. Ordenar Votos (Turno Mañana)")
        print("4. Mostrar listas con menos del 5% de votos")
        print("5. Mostrar turno con más votos")
        print("6. Verificar si hay Ballotage")
        print("7. Realizar segunda vuelta")
        print("8. Salir")
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            cargar_votos(matriz)
        elif opcion == 2:
            mostrar_votos(matriz)
        elif opcion == 3:
            ordenar_votos_mañana(matriz)
            mostrar_votos(matriz)
        elif opcion == 4:
            no_te_voto_nadie(matriz)
        elif opcion == 5:
            turno_mas_votado(matriz)
        elif opcion == 6:
            verificar_ballotage(matriz)
        elif opcion == 7:
            realizar_segunda_vuelta(matriz)
        elif opcion == 8:
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

menu()