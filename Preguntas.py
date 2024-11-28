import pygame
import os

def parse_csv(nombre_archivo:str): 
    '''
        Esta funcion parsea un archivo CSV de proyectos y lo devuelve en una lista de diccionarios \n
        Recibe como parametro un string que es el nombre del archivo \n
        Retorna la lista o False si no encontró el archivo \n
    '''
    lista_preguntas = [] 
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo,"r", encoding='utf-8') as archivo:
            primer_linea = archivo.readline()
            primer_linea = primer_linea.replace("\n","")
            lista_claves = primer_linea.split(",")
            for linea in archivo:
                linea_aux = linea.replace("\n", "")
                lista_valores = linea_aux.split(",") 
                diccionario_aux = {}
                for i in range(len(lista_claves)):
                    diccionario_aux[lista_claves[i]] = lista_valores[i]

                lista_preguntas.append(diccionario_aux)
        return lista_preguntas
    else:
        return False
    
lista_preguntas = parse_csv("preguntas.csv")