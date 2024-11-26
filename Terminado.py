import pygame
from Constantes import *
from Funciones import *
import os
import json
from datetime import datetime

pygame.init()

fondo = pygame.image.load("terminado.png")
fondo = pygame.transform.scale(fondo, VENTANA)

def generar_json(nombre_archivo:str,nuevo_jugador:list):
    if os.path.exists("Datos jugadores.json"):
        with open("Datos jugadores.json", "r") as archivo:
            lista_jugadores = json.load(archivo)
    else:
        lista_jugadores = []

    lista_jugadores.append(nuevo_jugador)

    with open("Datos jugadores.json", "w") as archivo:
        json.dump(lista_jugadores, archivo, indent=4)

fuente = pygame.font.SysFont("qatar-2022-book",40)
cuadro = {}
cuadro["superficie"] = pygame.Surface(CUADRO_TEXTO)
cuadro["rectangulo"] = cuadro["superficie"].get_rect()
cuadro['superficie'].fill(COLOR_BLANCO)
nombre = ""

def mostrar_fin_juego(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],datos_juego:dict) -> str:
    global nombre
    retorno = "terminado"



    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            #Estaria bueno forzarle al usuario que no pueda salir del juego hasta que guarde la puntuacion -> A gusto de ustedes
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            pass
        elif evento.type == pygame.KEYDOWN:
            bloc_mayus = pygame.key.get_mods() and pygame.KMOD_CAPS
            letra_presionada = pygame.key.name(evento.key)
            
            if letra_presionada == "backspace" and len(nombre) > 0:
                nombre = nombre[0:-1]#Elimino el ultimo
                cuadro["superficie"].fill(COLOR_BLANCO)
            
            if letra_presionada == "space":
                nombre += " "
            
            if len(letra_presionada) == 1:  
                if bloc_mayus != 0:
                    nombre += letra_presionada.upper()
                else:
                    nombre += letra_presionada

            if (letra_presionada == "return") and (len(nombre) > 0):
                    fecha_actual = datetime.now().strftime("%d/%m/%Y")
                    nuevo_jugador = {"nombre": nombre, "puntaje": datos_juego["puntuacion"], "fecha": fecha_actual}
                    generar_json("Datos jugadores.json",nuevo_jugador)
                    print(f"Nombre guardado en JSON: {nombre}")
                    cuadro['superficie'].fill(COLOR_NEGRO)
                    nombre = ""
                    reiniciar_datos_juego(datos_juego)
                    retorno = "menu"
            print(letra_presionada)
        
    pantalla.blit(fondo, (0, 0))
    
    cuadro["rectangulo"] = pantalla.blit(cuadro["superficie"],(340,300))
    mostrar_texto(cuadro["superficie"],nombre,(10,10),fuente,COLOR_NEGRO)
    mostrar_texto(pantalla,f"Usted obtuvo: {datos_juego["puntuacion"]} puntos",(250,220),fuente,COLOR_NEGRO)

    return retorno