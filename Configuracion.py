import pygame
from Constantes import *
from Funciones import mostrar_texto

pygame.init()

fuente_boton = pygame.font.SysFont("Arial Narrow",23)
fuente_volumen = pygame.font.SysFont("Arial Narrow",50)

boton_suma = {}
boton_suma["superficie"] = pygame.Surface(TAMAÑO_BOTON_VOLUMEN)
boton_suma["rectangulo"] = boton_suma["superficie"].get_rect()
boton_suma["superficie"].fill(COLOR_ROJO)
boton_resta = {}
boton_resta["superficie"] = pygame.Surface(TAMAÑO_BOTON_VOLUMEN)
boton_resta["rectangulo"] = boton_resta["superficie"].get_rect()
boton_resta["superficie"].fill(COLOR_ROJO)
boton_volver = {}
boton_volver["superficie"] = pygame.Surface(TAMAÑO_BOTON_VOLVER)
boton_volver["rectangulo"] = boton_volver["superficie"].get_rect()
boton_volver["superficie"].fill(COLOR_AZUL)

def mostrar_configuracion(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],datos_juego:dict) -> str:
    retorno = "configuraciones"
    
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_suma["rectangulo"].collidepoint(evento.pos):
                print("SUMA VOLUMEN")
                
                if datos_juego["volumen_musica"] < 100:
                    datos_juego["volumen_musica"] += 5
                CLICK_SONIDO.play()
            elif boton_resta["rectangulo"].collidepoint(evento.pos):
                print("RESTA VOLUMEN")
                if datos_juego["volumen_musica"] > 0:
                    datos_juego["volumen_musica"] -= 5
                CLICK_SONIDO.play()
            elif boton_volver["rectangulo"].collidepoint(evento.pos):
                print("VOLVER AL MENU")
                CLICK_SONIDO.play()
                retorno = "menu"
                
    pantalla.fill(COLOR_BLANCO)
    
    boton_suma["rectangulo"] = pantalla.blit(boton_suma['superficie'],(420,200))
    boton_resta["rectangulo"] = pantalla.blit(boton_resta['superficie'],(20,200))
    boton_volver["rectangulo"] = pantalla.blit(boton_volver['superficie'],(10,10))
    
    mostrar_texto(boton_suma["superficie"],"VOL +",(0,10),fuente_boton,COLOR_NEGRO)
    mostrar_texto(boton_resta["superficie"],"VOL -",(0,10),fuente_boton,COLOR_NEGRO)
    mostrar_texto(boton_volver["superficie"],"VOLVER",(10,10),fuente_boton,COLOR_BLANCO)
    mostrar_texto(pantalla,f"{datos_juego["volumen_musica"]} %",(200,200),fuente_volumen,COLOR_NEGRO)

    return retorno
                
