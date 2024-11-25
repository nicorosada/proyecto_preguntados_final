import pygame
import os

def parse_csv(nombre_archivo:str) -> bool: 

    lista_elementos = []
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo,"r") as archivo:
            primer_linea = archivo.readline()
            primer_linea = primer_linea.replace("\n","")
            lista_claves = primer_linea.split(",")
            for linea in archivo:
                linea_aux = linea.replace("\n","")
                lista_valores = linea_aux.split(",")
                diccionario_aux = {}
                for i in range(len(lista_claves)):
                    diccionario_aux[lista_claves[i]] = lista_valores[i]
                lista_elementos.append(diccionario_aux)
        return lista_elementos
    else:
        return False
    

def convertir_preguntas(lista_preguntas: list) -> list:
    """
    Convierte la lista de preguntas parseadas en un formato compatible con el juego.

    Args:
        lista_preguntas (list): Lista de diccionarios con las preguntas parseadas del CSV.

    Returns:
        list: Lista de preguntas en el formato esperado por el juego.
    """
    preguntas_juego = []
    for pregunta in lista_preguntas:
        nueva_pregunta = {
            "pregunta": pregunta["pregunta"],
            "opciones": [
                pregunta["respuesta_1"],
                pregunta["respuesta_2"],
                pregunta["respuesta_3"],
                pregunta["respuesta_4"],
            ],
            "correcta": int(pregunta["respuesta_correcta"]) - 1  # Convertir a índice base 0
        }
        preguntas_juego.append(nueva_pregunta)
    return preguntas_juego

lista_preguntas = parse_csv("Preguntas_Preguntados.csv")
convertir_preguntas(lista_preguntas)
