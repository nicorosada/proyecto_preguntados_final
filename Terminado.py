import pygame
from Constantes import *
from Funciones import mostrar_texto

pygame.init()

fuente = pygame.font.SysFont("qatar-2022-book",40)
cuadro = {}
cuadro["superficie"] = pygame.Surface(CUADRO_TEXTO)
cuadro["rectangulo"] = cuadro["superficie"].get_rect()
cuadro['superficie'].fill(COLOR_AZUL)
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
                cuadro["superficie"].fill(COLOR_AZUL)
            
            if letra_presionada == "space":
                nombre += " "
            
            if len(letra_presionada) == 1:  
                if bloc_mayus != 0:
                    nombre += letra_presionada.upper()
                else:
                    nombre += letra_presionada
        
        
    pantalla.fill(COLOR_BLANCO)
    cuadro["rectangulo"] = pantalla.blit(cuadro["superficie"],(200,200))
    mostrar_texto(cuadro["superficie"],nombre,(10,0),fuente,COLOR_BLANCO)
    mostrar_texto(pantalla,f"Usted obtuvo: {datos_juego["puntuacion"]} puntos",(250,100),fuente,COLOR_NEGRO)
    
    return retorno