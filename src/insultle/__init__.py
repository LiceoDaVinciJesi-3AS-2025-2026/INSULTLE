#INSULTLE
#Dafne Belardinelli, Edoardo Pani, Qian Qian Zhang

import pygame
import random

pygame.init()

Larghezza_Schermo = 822
Altezza_Schermo = 745

schermo = pygame.display.set_mode((Larghezza_Schermo, Altezza_Schermo)) 
pygame.display.set_caption("Insultle") 

imgSfondo = pygame.image.load("sfondoINSULTLE.jpg") 
imgSfondo = pygame.transform.scale(imgSfondo,(Larghezza_Schermo,Altezza_Schermo))

#FontTitolo = pygame.font.SysFont('Impact', 50)
FontLettere = pygame.font.SysFont('Impact', 60)

#Titolo = FontTitolo.render("INSULTLE", True, "#B5E61D") è brutto, per ora stiamo senza, no problem
letteraPremuta = ""

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        
        if event.type == pygame.KEYDOWN:
            letteraPremuta = event.unicode  # <-- prende la lettera premuta (chiesto a chat)
            
        #gli elementi si metto in ordine: sfondo, terzo, secondo e primo piano (vengono aggiunti sempre)
        schermo.blit(imgSfondo,(0,0) )
        #schermo.blit(Titolo, (50,50))
        #schermo.blit(letteraPremuta, (15,25)) <-- questo è sbagliato perchè blit aggiorna lo schermo aggiungendo img e non str, quindi:

        testoResoImg = FontLettere.render(f"{letteraPremuta.upper()}", True , "black") #render renderizza una scritta 
        schermo.blit(testoResoImg, (200, 20))
        
        #.flip aggiorna lo schermo, lasciamolo SEMPRE alla fine
        pygame.display.flip()
        
        #QIAN : devo finire di scrivere, devo fa il codice che mi mette le lettere in caselle diverse
        #QIAN : DAFNE NON TOCCCARE NULLA!!!!
        
pygame.quit()
