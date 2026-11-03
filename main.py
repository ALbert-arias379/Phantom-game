import sys
import pygame 

pygame.init()

#640x350  resolución provisional
ANCHO = 640 
ALTO = 350
screen = pygame.display.set_mode((ANCHO, ALTO))


pygame.display.set_caption("sudo Sentai Kioprager")

#Fondo del menu
BG = pygame.image.load("assets/bg.jpg")


# Rescalamos la imagen para que concuerde con el tamaño de la ventana
BG = pygame.transform.scale(BG, (640, 350)) # 


Buttom = pygame.Rect(250, 140, 140, 50) #Boton generico


# Paletas de colores
BLANCO =( 255,255,255)
NEGRO = (0,0,0)
ROJO = (255,0,0)
VERDE = (0,255,0)
AZUL = (0,0,255)



def main_menu():
    running = True
    count = 0 # contador sorpresa

    while running:

        # bucle para obtener eventos
        for event  in pygame.event.get():
            
            if event.type == pygame.QUIT: #cerrar ventana, da igual uso niri
                running = False

            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_q:                 #permite leer el ratón
                    running = False

        # Establecer el fondo
        screen.blit(BG, (0,0))

        # Dibujar icono de perfil, le pondre imagen luego
        pygame.draw.circle(screen, BLANCO, (ANCHO // 2, ALTO // 2), 40)

        #dibujar boton
        pygame.draw.rect(screen, ROJO, Buttom)

        # Obtener posición del mouse
        mouse_pos = pygame.mouse.get_pos()


                  #Colisición
        if Buttom.collidepoint(mouse_pos):
            pygame.draw.rect(screen,AZUL,Buttom) # Dibujamos otro boton igual arriba del rojo para simular cambio de color

            if event.type == pygame.MOUSEBUTTONDOWN: # Presionar 
                count +=1 
                if count>10:
                    print("HAZ SIDO HACKEADO")
                else:
                    print(f"Si le das otras {10-count} te ganaras un premio")

            


        pygame.display.flip() # Actualiza 




    #Cierra de forma segura
    pygame.quit()
    sys.exit()

   






main_menu()
# pygame.draw.rect(screen, ROJO, (10,10,100,100 ))
# pygame.draw.rect(screen, VERDE, (-10,10,100,100 ))
# pygame.draw.rect(screen, AZUL, (-10,-10,100,100 ))
# pygame.draw.rect(screen, BLANCO, (10,-10,100,100 ))
# # no se porque las posiciones no me estan cuadrando
 


