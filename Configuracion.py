import pygame
from Constantes import *
from Funciones import mostrar_texto

pygame.init()

# Fuentes de los textos
fuente_boton = pygame.font.SysFont("qatar-2022-book", 23)
fuente_volumen = pygame.font.SysFont("qatar-2022-book", 35)

# Cargar imágenes para los botones
imagen_bajar_volumen = pygame.image.load("boton_configuracion.png")
imagen_subir_volumen = pygame.image.load("boton_configuracion.png")
imagen_mutear_volumen = pygame.image.load("boton_configuracion.png")
imagen_desmutear_volumen = pygame.image.load("boton_configuracion.png")
imagen_menu = pygame.image.load("menu_config.png")
imagen_volver = pygame.image.load("volver.png")

# Cargar imagen de fondo
imagen_fondo = pygame.image.load("fondo_config.png")

# Crear botones con imágenes y sus rectángulos
boton_suma = {
    "superficie": imagen_subir_volumen,
    "rectangulo": imagen_subir_volumen.get_rect(),
}
boton_resta = {
    "superficie": imagen_bajar_volumen,
    "rectangulo": imagen_bajar_volumen.get_rect(),
}
boton_volver = {
    "superficie": imagen_volver,
    "rectangulo": imagen_volver.get_rect(),
}
boton_mutear = {
    "superficie":imagen_mutear_volumen,
    "rectangulo":imagen_mutear_volumen.get_rect(),
}
boton_desmutear = {
    "superficie":imagen_desmutear_volumen,
    "rectangulo":imagen_desmutear_volumen.get_rect(),
}

def mostrar_configuracion(
    pantalla: pygame.Surface, cola_eventos: list[pygame.event.Event], datos_juego: dict) -> str:
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
            elif boton_mutear["rectangulo"].collidepoint(evento.pos):
                datos_juego["volumen_musica"] = 0
                print("MUTEAR")
            elif boton_desmutear["rectangulo"].collidepoint(evento.pos):
                if datos_juego["volumen_musica"] == 0:
                    datos_juego ["volumen_musica"] += 100
                    print("DESMUTEAR")
            elif boton_volver["rectangulo"].collidepoint(evento.pos):
                print("VOLVER AL MENU")
                CLICK_SONIDO.play()
                retorno = "menu"

    # Dibujar imagen de fondo
    pantalla.blit(imagen_fondo, (0, 0))
    pantalla.blit(imagen_menu,(165,70))

    # Dibujar botones con imágenes
    boton_suma["rectangulo"] = pantalla.blit(boton_suma["superficie"], (200, 200))
    boton_resta["rectangulo"] = pantalla.blit(boton_resta["superficie"], (520, 200))
    boton_mutear["rectangulo"] = pantalla.blit(boton_mutear["superficie"], (200, 370))
    boton_desmutear["rectangulo"] = pantalla.blit(boton_desmutear["superficie"], (520, 370))
    boton_volver["rectangulo"] = pantalla.blit(boton_volver["superficie"], (10, 10))
    
    # Mostramos textos de los botones
    mostrar_texto(boton_suma["superficie"], "Vol +", (80, 13), fuente_boton, COLOR_BLANCO)
    mostrar_texto(boton_resta["superficie"], "Vol -", (80, 13), fuente_boton, COLOR_BLANCO)
    mostrar_texto(boton_mutear["superficie"], "Mutear", (65, 13), fuente_boton, COLOR_BLANCO)
    mostrar_texto(boton_desmutear["superficie"], "Desmutear", (45, 13), fuente_boton, COLOR_BLANCO)
    mostrar_texto(pantalla,f"{datos_juego['volumen_musica']} %",(425, 460),fuente_volumen,COLOR_BLANCO)

    return retorno


                
