import pygame
from Constantes import *
from Funciones import mostrar_texto

pygame.init()

# Fuente del menu
fuente_menu = pygame.font.SysFont("qatar-2022-book",25)


# Crea la superficie con las imagenes cargadas y el area para accionar
lista_botones = []
for i in range(4):
    boton = {}
    boton["superficie"] = pygame.image.load("boton_nuevo.png")
    boton["rectangulo"] = boton["superficie"].get_rect()
    lista_botones.append(boton)

# Carga la imagen del fondo y la escala
fondo = pygame.image.load("imagen_fondo.jpg")
fondo = pygame.transform.scale(fondo,VENTANA)

def mostrar_menu(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event])-> str:
    #Gestionar eventos:
    retorno = "menu"
    for evento in cola_eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(lista_botones)): 
                if lista_botones[i]["rectangulo"].collidepoint(evento.pos):
                    CLICK_SONIDO.play()
                    if i == BOTON_SALIR:
                        retorno = "salir"  
                    elif i == BOTON_JUGAR:
                        retorno = "juego"  
                    elif i == BOTON_PUNTUACIONES:
                        retorno = "rankings"
                    elif i == BOTON_CONFIG:
                        retorno = "configuraciones"        
        elif evento.type == pygame.QUIT:
            retorno = "salir"
                
    #Actualizar el juego:
    
    #Dibuja la imagen de fondo
    pantalla.blit(fondo,(0,0))
    
    # Dibuja los botones del menu
    lista_botones[0]["rectangulo"] = pantalla.blit(lista_botones[0]["superficie"],(-80,115))
    lista_botones[1]["rectangulo"] = pantalla.blit(lista_botones[1]["superficie"],(0,195))
    lista_botones[2]["rectangulo"] = pantalla.blit(lista_botones[2]["superficie"],(0,275))
    lista_botones[3]["rectangulo"] = pantalla.blit(lista_botones[3]["superficie"],(-80,355))

    # Muestra el texto de los botones
    mostrar_texto(lista_botones[0]["superficie"],"Jugar",(180,23),fuente_menu,COLOR_NEGRO)
    mostrar_texto(lista_botones[1]["superficie"],"Configuracion",(130,25),fuente_menu,COLOR_NEGRO)
    mostrar_texto(lista_botones[2]["superficie"],"Puntuaciones",(130,25),fuente_menu,COLOR_NEGRO)
    mostrar_texto(lista_botones[3]["superficie"],"Salir",(180,25),fuente_menu,COLOR_NEGRO)
    
    return retorno