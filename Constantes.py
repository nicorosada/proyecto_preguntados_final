import pygame
pygame.init()

COLOR_BLANCO = (255,255,255)
COLOR_NEGRO = (0,0,0)
COLOR_VERDE = (0,255,0)
COLOR_ROJO = (255,0,0)
COLOR_AZUL = (0,0,255)
COLOR_VIOLETA = (134,23,219)
ANCHO = 950
ALTO = 600
VENTANA = (ANCHO,ALTO)
FPS = 60

BOTON_JUGAR = 0
BOTON_CONFIG = 1
BOTON_PUNTUACIONES = 2
BOTON_SALIR = 3

TAMAÑO_PREGUNTA = (400,200)
TAMAÑO_RESPUESTA = (250,60)
TAMAÑO_BOTON = (250,60)
CUADRO_TEXTO = (250,50)
TAMAÑO_BOTON_VOLUMEN = (60,60)
TAMAÑO_BOTON_VOLVER = (100,40)
CLICK_SONIDO = pygame.mixer.Sound("sonido_click_futbol.mp3")
# ERROR_SONIDO = pygame.mixer.Sound("error.mp3")

CANTIDAD_VIDAS = 3
PUNTUACION_ACIERTO = 100
PUNTUACION_ERROR = 25