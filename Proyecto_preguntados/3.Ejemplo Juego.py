import pygame
from Constantes import *
from Preguntas import *
from Funciones import *

#Inicializar pygame
pygame.init()

#Configuraciones básicas
#Nombre del proyecto
pygame.display.set_caption("MI PRIMER JUEGO 114")

#Icono
icono = pygame.image.load("icono-10.png")
pygame.display.set_icon(icono)

#Generamos nuestra primer superficie

#Configurar la pantalla
pantalla = pygame.display.set_mode(VENTANA)
corriendo = True

#SONIDOS
sonido_click = pygame.mixer.Sound("sonido_click_futbol.mp3")
# sonido_error = pygame.mixer.Sound("error.mp3")

datos_juego = {"puntuacion":0,"vidas":CANTIDAD_VIDAS,"nombre":""}

#Creo la cuadro de la pregunta
cuadro_pregunta = {}
#La idea es que se cargue de una imagen
cuadro_pregunta["superficie"] = pygame.Surface(TAMAÑO_PREGUNTA)
cuadro_pregunta["rectangulo"] = cuadro_pregunta["superficie"].get_rect()

cartas_respuestas = []

for i in range(3):
    cuadro_respuesta = {}
    cuadro_respuesta["superficie"] = pygame.Surface(TAMAÑO_RESPUESTA)
    cuadro_respuesta["rectangulo"] = cuadro_respuesta["superficie"].get_rect()
    cartas_respuestas.append(cuadro_respuesta)

#MUSICA

# pygame.mixer.init() #Inicializo mixer para manipular la musica
# pygame.mixer.music.load("musica.mp3") #Cargo musica de fondo
# pygame.mixer.music.set_volume(0.05)
# pygame.mixer.music.play()#Se ejecuta una vez
# pygame.mixer.music.play(-1)#Se ejecuta constatemente

#Creo un reloj
clock = pygame.time.Clock()

#TEXTO 

fuente_pregunta = pygame.font.SysFont("Arial Narrow",30)
fuente_respuesta = pygame.font.SysFont("Arial Narrow",23)
fuente_texto = pygame.font.SysFont("Arial Narrow",25)

mezclar_lista(lista_preguntas)
indice = 0
pregunta_actual = lista_preguntas[indice]
bandera_respuesta = False


#2.Bucle principal -> Es el bucle que se ejecuta cuando el juego esta activo
while corriendo:
    #3.Definir el tiempo en el que las imagenes se van a actualizar (FPS)
    clock.tick(FPS)  
    
    #NO HACE FALTA SI USAN IMAGEN
    cuadro_pregunta["superficie"].fill(COLOR_ROJO)
    
    for carta in cartas_respuestas:
        carta["superficie"].fill(COLOR_AZUL)
        
    if bandera_respuesta:
        pygame.time.delay(500)
        bandera_respuesta = False
    
    pregunta_actual = lista_preguntas[indice]

        
    # if bandera_respuesta:
    #     pygame.time.delay(500)
    #     bandera_respuesta = False
    
    #4. Gestionar eventos:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            print("SALIENDO")
            corriendo = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(cartas_respuestas)):
                if cartas_respuestas[i]['rectangulo'].collidepoint(evento.pos):
                    respuesta_usuario = (i + 1)
                    
                    if verificar_respuesta(datos_juego,pregunta_actual,respuesta_usuario):
                        #Aca recomiendo un sonido de respuesta correcta
                        sonido_click.play()
                        cartas_respuestas[i]['superficie'].fill(COLOR_VERDE)
                        print("RESPUESTA CORRECTA")
                    else:
                        sonido_error.play()
                        cartas_respuestas[i]['superficie'].fill(COLOR_ROJO)
                        print("RESPUESTA INCORRECTA")
                    
                    print(f"SE HIZO CLICK EN UNA RESPUESTA {respuesta_usuario}")
                    bandera_respuesta = True
                    
                    if indice == len(lista_preguntas):
                        indice = 0
                        mezclar_lista(lista_preguntas)
                    indice += 1

    
    #5. Actualizar el juego: 
    
    #6.Dibujar pantalla y las otras superficies
    #texto_pregunta = fuente_pregunta.render(f"{pregunta_actual["pregunta"]}",False,COLOR_NEGRO)
    #cuadro_pregunta["superficie"].blit(texto_pregunta,(20,20))
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
    
    
    
    #Imprimir texto


    #7.Actualiza la pantalla
    pygame.display.flip()
pygame.quit()