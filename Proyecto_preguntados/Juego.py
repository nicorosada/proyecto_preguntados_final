import pygame
from Constantes import *
from Preguntas import *
from Funciones import *

pygame.init()

cuadro_pregunta = {}
cuadro_pregunta["superficie"] = pygame.Surface(TAMAÑO_PREGUNTA)
cuadro_pregunta["rectangulo"] = cuadro_pregunta["superficie"].get_rect()

cartas_respuestas = []
for i in range(3):
    cuadro_respuesta = {}
    cuadro_respuesta["superficie"] = pygame.Surface(TAMAÑO_RESPUESTA)
    cuadro_respuesta["rectangulo"] = cuadro_respuesta["superficie"].get_rect()
    cartas_respuestas.append(cuadro_respuesta)

fuente_pregunta = pygame.font.SysFont("Arial Narrow",30)
fuente_respuesta = pygame.font.SysFont("Arial Narrow",23)
fuente_texto = pygame.font.SysFont("Arial Narrow",25)
mezclar_lista(lista_preguntas)
indice = 0 #INMUTABLE -> En la funcion las declaro como global
bandera_respuesta = False #INMUTABLE -> En la funcion las declaro como global

def mostrar_juego(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],datos_juego:dict) -> str:
    global indice
    global bandera_respuesta
    
    retorno = "juego"
    
    cuadro_pregunta["superficie"].fill(COLOR_ROJO)
    for carta in cartas_respuestas:
        carta["superficie"].fill(COLOR_AZUL)
        
    if bandera_respuesta:
        pygame.time.delay(500)
        bandera_respuesta = False
        
    pregunta_actual = lista_preguntas[indice]
    
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(cartas_respuestas)):
                if cartas_respuestas[i]['rectangulo'].collidepoint(evento.pos):
                    respuesta_usuario = (i + 1)
                    
                    if verificar_respuesta(datos_juego,pregunta_actual,respuesta_usuario):
                        #Aca recomiendo un sonido de respuesta correcta
                        CLICK_SONIDO.play()
                        cartas_respuestas[i]['superficie'].fill(COLOR_VERDE)
                        print("RESPUESTA CORRECTA")
                    else:
                        # ERROR_SONIDO.play()
                        cartas_respuestas[i]['superficie'].fill(COLOR_ROJO)
                        retorno = "terminado"
                        print("RESPUESTA INCORRECTA")
                    
                    print(f"SE HIZO CLICK EN UNA RESPUESTA {respuesta_usuario}")
                    bandera_respuesta = True
                    
                    if indice == len(lista_preguntas):
                        indice = 0
                        mezclar_lista(lista_preguntas)
                    indice += 1
    
    mostrar_texto(cuadro_pregunta["superficie"],f"{pregunta_actual["pregunta"]}",(20,20),fuente_pregunta,COLOR_NEGRO)
    mostrar_texto(cartas_respuestas[0]["superficie"],f"{pregunta_actual["respuesta_1"]}",(20,20),fuente_respuesta,COLOR_BLANCO)
    mostrar_texto(cartas_respuestas[1]["superficie"],f"{pregunta_actual["respuesta_2"]}",(20,20),fuente_respuesta,COLOR_BLANCO)
    mostrar_texto(cartas_respuestas[2]["superficie"],f"{pregunta_actual["respuesta_3"]}",(20,20),fuente_respuesta,COLOR_BLANCO)
    
    pantalla.fill(COLOR_BLANCO)
    pantalla.blit(cuadro_pregunta["superficie"],(80,80))
    
    cartas_respuestas[0]['rectangulo'] = pantalla.blit(cartas_respuestas[0]['superficie'],(125,245))
    cartas_respuestas[1]['rectangulo'] = pantalla.blit(cartas_respuestas[1]['superficie'],(125,315))
    cartas_respuestas[2]['rectangulo'] = pantalla.blit(cartas_respuestas[2]['superficie'],(125,385))
    
    mostrar_texto(pantalla,f"PUNTUACION: {datos_juego['puntuacion']}",(10,10),fuente_texto,COLOR_NEGRO)
    mostrar_texto(pantalla,f"VIDAS: {datos_juego['vidas']}",(10,40),fuente_texto,COLOR_NEGRO)
    
    return retorno