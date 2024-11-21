import pygame
from Constantes import *
from Menu import *
from Juego import *
from Configuracion import *
from Rankings import *
from Terminado import *

#Configuraciones Basicas
pygame.init()
pygame.mixer.init()
pygame.display.set_caption("MI PRIMER JUEGO 114")
icono = pygame.image.load("icono-10.png")
pygame.display.set_icon(icono)
pantalla = pygame.display.set_mode(VENTANA)
corriendo = True
reloj = pygame.time.Clock()
datos_juego = {"puntuacion":0,"vidas":CANTIDAD_VIDAS,"nombre":"","volumen_musica":100}
ventana_actual = "menu"
bandera_musica = False

#Ciclo de vida
while corriendo:
    reloj.tick(FPS)
    cola_eventos = pygame.event.get()
    
    if ventana_actual == "menu":
        ventana_actual = mostrar_menu(pantalla,cola_eventos)
    elif ventana_actual == "juego":
        if bandera_musica == False:
            porcentaje_volumen = datos_juego["volumen_musica"] / 100
            pygame.mixer.music.load("musicaa.mp3")
            pygame.mixer.music.set_volume(porcentaje_volumen)
            pygame.mixer.music.play(-1)
            bandera_musica = True
        ventana_actual = mostrar_juego(pantalla,cola_eventos,datos_juego)
    elif ventana_actual == "configuraciones":
        ventana_actual = mostrar_configuracion(pantalla,cola_eventos,datos_juego)
    elif ventana_actual == "rankings":
        ventana_actual = mostrar_rankings(pantalla,cola_eventos)
    elif ventana_actual == "terminado":
        if bandera_musica == True:
            pygame.mixer.music.stop()
            bandera_musica = False
        ventana_actual = mostrar_fin_juego(pantalla,cola_eventos,datos_juego)
    elif ventana_actual == "salir":
        corriendo = False
    
    #Actualizar cambios
    pygame.display.flip()

pygame.quit()
    