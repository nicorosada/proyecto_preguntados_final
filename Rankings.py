import pygame
from Constantes import *
from Funciones import mostrar_texto
import json
import os

pygame.init()




fuente = pygame.font.SysFont("qatar-2022-book",22)
fuente_boton = pygame.font.SysFont("qatar-2022-book",23)
imagen_volver = pygame.image.load("volver.png")
imagen_menu = pygame.image.load("top10.png")
boton_volver = {
    "superficie": imagen_volver,
    "rectangulo": imagen_volver.get_rect(),
}



def parse_json(nombre_archivo:str):
    '''
        Recibe como parámetro el archivo a convertir
        Convierte un archivo JSON a una lista de diccionarios
        Retorna la lista de diccionarios
    '''
    lista_elementos = []   
    if os.path.exists("Datos jugadores.json"):
        with open("Datos jugadores.json", "r") as archivo:
            lista_elementos = json.load(archivo)
    else:
        lista_elementos = []
    
    return lista_elementos

def ordenar_lista_ranking(lista_elementos:list)->list:
    # lista_elementos = parse_json("Datos jugadores.json")
    lista_elementos.sort(key=lambda jugador: jugador["puntaje"], reverse=True)
    # Devolver solo los 10 mejores jugadores
    return lista_elementos[:10]


def mostrar_rankings(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event]):
    retorno = "rankings"
    
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_volver["rectangulo"].collidepoint(evento.pos):
                print("VOLVER AL MENU")
                CLICK_SONIDO.play()
                retorno = "menu"
    
    pantalla.fill(COLOR_VIOLETA)
    pantalla.blit(imagen_menu,(165,70))
    boton_volver["rectangulo"] = pantalla.blit(boton_volver["superficie"],(10,10))
    mostrar_texto(boton_volver["superficie"],"Volver",(10,10),fuente_boton,COLOR_BLANCO)
    # mostrar_texto(pantalla,f"Aca se debe mostrar el Top 10",(20,200),fuente,COLOR_NEGRO)
    lista_elementos = parse_json("Datos jugadores.json")
    lista_elementos = ordenar_lista_ranking(lista_elementos)



    y = 150

    if lista_elementos == []:
        mostrar_texto(pantalla,"NO SE REGISTRARON PARTIDAS",(315,275),fuente,COLOR_BLANCO)
    else:
        for i in range(len(lista_elementos)):
            mostrar_texto(pantalla,f"{lista_elementos[i]['nombre']} ",(335,y),fuente,COLOR_BLANCO)
            mostrar_texto(pantalla,f"{i+1}.",(290,y),fuente,COLOR_BLANCO)
            mostrar_texto(pantalla,f"{lista_elementos[i]['puntaje']} ",(600,y),fuente,COLOR_BLANCO)
            y += 35

    return retorno              

