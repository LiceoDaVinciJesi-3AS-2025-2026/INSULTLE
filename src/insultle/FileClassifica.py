import pygame

def classifica() -> None:
    
    # Questa funzione permette di visualizzare la classifica se si clicca sul tasto "CLASSIFICA"
    
    pygame.init()

    # dimensioni della finestra, uguali a quelle del gioco
    Larghezza_Schermo = 822
    Altezza_Schermo = 745

    # creo la finestra pygame
    schermo = pygame.display.set_mode((Larghezza_Schermo, Altezza_Schermo))

    # font del titolo e del testo
    FontTitolo = pygame.font.SysFont('Impact', 70)
    FontTesto = pygame.font.SysFont('Impact', 30)

    # apre il file della classifica e ne legge tutte le righe
    with open("fileVincente.txt", "r") as file:
        righe = file.readlines() 

    running = True
    while running:

        # sfondo bianco
        schermo.fill("white")

        # titolo CLASSIFICA
        titolo = FontTitolo.render("CLASSIFICA", True, "green")
        schermo.blit(titolo,(250,50))

        # posizione iniziale del testo
        y = 200

        # mostra tutte le righe del file
        for riga in righe:

            testo = FontTesto.render(riga.strip(), True, "black")
            schermo.blit(testo, (50,y))

            # sposta la riga successiva più in basso
            y += 40

        # controllo gli eventi con i tasti della tastiera
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        pygame.display.flip()