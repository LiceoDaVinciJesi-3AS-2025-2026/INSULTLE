#funzioni
#libreria standard
import random
import time
from datetime import date
from pathlib import Path

#librerie pip
import pygame
from platformdirs import PlatformDirs

#moduli del mio package
from insultle.resources import *


#-------- NOME GIOCATORE, SFONDO E ALTRE SCRITTE ----------------
def nome():
    """
    Funzione che gestisce la schermata di inserimento del nome giocatore.
    Crea una finestra dove il giocatore può digitare il proprio nome.
    Restituisce il nome inserito quando si preme INVIO.
    """

    Larghezza_Schermo = 822
    Altezza_Schermo = 745
    schermo = pygame.display.set_mode((Larghezza_Schermo, Altezza_Schermo))
    pygame.display.set_caption("Insultle")
    FontLettere = pygame.font.SysFont('Impact', 60)

    #carica l'immagine di sfondo in base alle variabili sopra scritte
    percorsoImgSfondo = get_image("sfondoINSULTLE.jpg")
    imgSfondo = pygame.image.load(percorsoImgSfondo)
    imgSfondo = pygame.transform.scale(imgSfondo, (Larghezza_Schermo, Altezza_Schermo))

    nome_giocatore = ""  #stringa vuota in cui andrà aggiunto il nome

    runningNome = True

    while runningNome:
        #esamino tutto ciò che succede
        for event in pygame.event.get():

            #se è la X rossa in alto a destra il gioco finisce
            if event.type == pygame.QUIT:
                #finisce il gioco
                runningNome = False
                return ""

            #se l'evento è un tasto premuto analizzo quale tasto è
            if event.type == pygame.KEYDOWN:

                #tasto invio
                if event.key == pygame.K_RETURN:
                    if nome_giocatore.strip():  # Evita nomi vuoti
                        return nome_giocatore   #restituisce il nome

                #tasto canc
                elif event.key == pygame.K_BACKSPACE:
                    nome_giocatore = nome_giocatore[:-1]  #cancella l'ultimo carattere
                #qualunque altro tasto
                else:
                    if len(nome_giocatore) < 20:  # Limita lunghezza nome
                        nome_giocatore += event.unicode  #aggiunge il carattere digitato al nome del giocatore

        #sfondo
        schermo.blit(imgSfondo, (0, 0))

        #scritta
        testoDomanda = FontLettere.render("INSERISCI IL TUO NOME", True, "black")
        schermo.blit(testoDomanda, (150, 200))

        #rettangolo bianco dove va visualizzato il nome
        rect_nome = pygame.Rect(200, 300, 400, 80)
        pygame.draw.rect(schermo, "black", rect_nome)

        # nome scritto
        testo_nome = FontLettere.render(nome_giocatore, True, "white")
        schermo.blit(testo_nome, (rect_nome.x + 10, rect_nome.y + 10))

        pygame.display.flip()


#---------------- VITTORIA ----------------
def vittoria(nome_giocatore, tempo):
    """
    In caso di vittoria:
    - Ferma la musica di sottofondo
    - Riproduce il suono di vittoria
    - Salva il risultato su file
    """
    global giocoFinito, percorsoFileVincente, suonoVittoria
    
    pygame.mixer.music.stop()  #fermo la musica di sottofondo
    
    try:
        suonoVittoria.play()  #metto il suono di vittoria
    except:
        print("Suono vittoria non trovato")
    
    giocoFinito = True  #modifico la variabile globale
    
    # Salva solo il risultato (senza testo pubblicitario)
    with open(percorsoFileVincente, "a") as file:
        file.write(f"{nome_giocatore},{tempo}\n")
    
    print(f"VITTORIA! {nome_giocatore} ha vinto in {tempo} secondi!")


#---------------- SCONFITTA ----------------
def sconfitta():
    """
    In caso di sconfitta:
    - Segnala la sconfitta
    - Salva su file la parola segreta
    """
    global giocoFinito, parolaSceltaComputer, percorsoFileVincente, suonoSconfitta
    
    pygame.mixer.music.stop()  #fermo la musica di sottofondo
    
    try:
        suonoSconfitta.play()  #metto il suono di sconfitta
    except:
        print("Suono sconfitta non trovato")
    
    giocoFinito = True  #modifico la variabile globale
    
    with open(percorsoFileVincente, "a") as file:
        file.write(f"SCONFITTA,parola:{parolaSceltaComputer}\n")
    
    print(f"SCONFITTA! La parola era: {parolaSceltaComputer}")


#---------------- SCHERMATA INIZIALE ----------------
def main():
    """
    Mostra la schermata principale con le regole e due pulsanti:
    - GIOCA: avvia una partita normale con parola casuale
    - PAROLA DEL GIORNO: avvia una partita con la parola del giorno
    - CLASSIFICA: mostra la classifica
    """
    global giocoFinito, parolaSceltaComputer, percorsoFileVincente, suonoSconfitta, suonoVittoria
    
    #inizializzazione di Pygame e del mixer audio
    pygame.init()  #fondamentale per il gioco (inializza tutto)
    pygame.mixer.init()  #fondamentale per i suoni
    
    #configurazione delle directory (cartella del computer) dove vengono salvati i file per il gioco, si chiamerà "insultle"
    dirs = PlatformDirs("insultle", ensure_exists=True)
    percorsoFileVincente = dirs.user_data_dir + "/fileVincente.txt"
    
    #caricamento e configurazione degli effetti sonori
    percorsoSuonoSconfitta = get_sound("suonoSconfitta.mp3")
    percorsoSuonoVittoria = get_sound("suonoVittoria.mp3")
    suonoSconfitta = pygame.mixer.Sound(percorsoSuonoSconfitta)
    suonoVittoria = pygame.mixer.Sound(percorsoSuonoVittoria)
    suonoSconfitta.set_volume(0.7)
    suonoVittoria.set_volume(0.7)
    
    #variabili globali
    giocoFinito = False
    parolaSceltaComputer = ""  #cambia parola ogni volta che rinizia il gioco
    
    #imposto le variabili per lo sfondo
    Larghezza_Schermo = 822
    Altezza_Schermo = 745
    schermo = pygame.display.set_mode((Larghezza_Schermo, Altezza_Schermo))
    pygame.display.set_caption("Insultle")
    FontLettere = pygame.font.SysFont('Impact', 60)
    
    #parole da indovinare
    ParoleComputer = ["ASINO", "CAGNA", "CAPRA", "CLOWN", "CESSO", "EBETE", "FESSO", "FOLLE", "FALSO", "GOFFO", "LENTO", "LONZA", "MATTO", "MOLLE", "MONCO", "MERDA", "PAZZO", "PIGRO", "PIPPA", "ORCO", "PORCO", "PIRLA", "RATTO", "RINCO", "ROZZO", "SCEMO", "SERPE", "TARDO", "TONTO", "VACCA", "VERME"]
    
    #carico le immagini
    percorsoImgSfondo = get_image("sfondoBIANCO.jfif")
    imgSfondo = pygame.image.load(percorsoImgSfondo)
    imgSfondo = pygame.transform.scale(imgSfondo, (Larghezza_Schermo, Altezza_Schermo))
    percorsoImgRegole = get_image("RegoleInsultle.png")
    imgRegole = pygame.image.load(percorsoImgRegole)
    imgRegole = pygame.transform.scale(imgRegole, (400, 400))
    
    #creo tre tasti che mi portano al gioco vero e proprio
    tasti_mouse = {
        "GIOCA": pygame.Rect(150, 510, 220, 70),
        "PAROLA DEL GIORNO": pygame.Rect(450, 510, 250, 70),
    }
    
    runningMain = True
    while runningMain:
        #mostro le regole e lo sfondo bianco
        schermo.blit(imgSfondo, (0, 0))
        schermo.blit(imgRegole, (200, 50))
        
        #disegno pulsanti
        for tasto, rect in tasti_mouse.items():
            pygame.draw.rect(schermo, "green", rect)
            testo = FontLettere.render(tasto, True, "black")
            # Centra il testo nel rettangolo
            testo_rect = testo.get_rect(center=rect.center)
            schermo.blit(testo, testo_rect)
        
        #analizzo ogni evento
        for event in pygame.event.get():
            #se clicco la X in alto a destra
            if event.type == pygame.QUIT:
                runningMain = False
                pygame.quit()
                return
            
            #se clicchi un tasto
            if event.type == pygame.KEYDOWN:
                #se è il tasto esc
                if event.key == pygame.K_ESCAPE:
                    runningMain = False
                    pygame.quit()
                    return
            
            #se clicco un tasto del mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos_mouse = pygame.mouse.get_pos()
                
                for tasto, rect in tasti_mouse.items():
                    if rect.collidepoint(pos_mouse):
                        if tasto == "GIOCA":
                            parolaSpeciale = False
                            nome_giocatore = nome()
                            if nome_giocatore == "":
                                break
                            parolaSceltaComputer = random.choice(ParoleComputer)
                            gioco(nome_giocatore, parolaSceltaComputer, parolaSpeciale, ParoleComputer)
                            runningMain = False
                        
                        elif tasto == "PAROLA DEL GIORNO":
                            parolaSpeciale = True
                            nome_giocatore = nome()
                            if nome_giocatore == "":
                                break
                            #SELEZIONE PAROLA DEL GIORNO
                            oggi = date.today().day
                            if oggi - 1 == 27:
                                oggi = 14
                            elif oggi - 1 == 28:
                                oggi = 15
                            elif oggi - 1 == 29:
                                oggi = 16
                            elif oggi - 1 == 30:
                                oggi = 17
                            
                            parolaSceltaComputer = ParoleComputer[(oggi - 1)]
                            gioco(nome_giocatore, parolaSceltaComputer, parolaSpeciale, ParoleComputer)
                            runningMain = False
                        
                        elif tasto == "CLASSIFICA":
                            classifica()
        
        #aggiorno lo schermo
        pygame.display.flip()


#---------------- GIOCO ----------------
def gioco(nome_giocatore, parolaSceltaComputer, parolaSpeciale, ParoleComputer):
    """
    Funzione principale del gioco:
    - Gestisce la logica di Wordle con parole di 5 lettere
    - Permette input da tastiera fisica e tastiera virtuale cliccabile
    - Mostra feedback colorati (verde: lettera giusta posizione giusta, giallo: lettera giusta posizione sbagliata, rosso: lettera sbagliata)
    - Include timer, musica e gestione tentativi
    """
    global giocoFinito, percorsoFileVincente, suonoVittoria, suonoSconfitta
    
    giocoFinito = False
    
    #variabili sfondo
    Larghezza_Schermo = 822
    Altezza_Schermo = 745
    schermo = pygame.display.set_mode((Larghezza_Schermo, Altezza_Schermo))
    pygame.display.set_caption("Insultle")
    
    #carico sfondo
    PercorsoImgSfondo = get_image("sfondoINSULTLE.jpg")
    imgSfondo = pygame.image.load(PercorsoImgSfondo)
    imgSfondo = pygame.transform.scale(imgSfondo, (Larghezza_Schermo, Altezza_Schermo))
    #carico immagine della casa che porterà il giocatore al menù iniziale
    PercorsoImgCasa = get_image("casa.png")
    imgCasa = pygame.image.load(PercorsoImgCasa)
    imgCasa = pygame.transform.scale(imgCasa, (50, 50))
    #carico immagine tasto retry che fa ripartire il gioco da capo
    PercorsoImgRetry = get_image("retry.jpg")
    imgRetry = pygame.image.load(PercorsoImgRetry)
    imgRetry = pygame.transform.scale(imgRetry, (50, 50))
    
    FontLettere = pygame.font.SysFont('Impact', 60)
    
    #apre il file vocabolario (le parole accettabili) e togli lo spazio finale da ogni parola
    percorsoFileVocabolario = get_data("Vocabolario.txt")
    paroleAccettabili = []
    with open(percorsoFileVocabolario, "r") as fileVocabolario:
        for riga in fileVocabolario:
            parola = riga.strip().upper()  # pulisco la stringa da \n e la rendo maiuscola
            paroleAccettabili.append(parola)
    
    #avvia la musica di sottofondo
    PercorsoSottofondo = get_sound("suonoSottofondo.mp3")
    pygame.mixer.music.load(PercorsoSottofondo)
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(-1)  #rendo quella musica un loop
    
    # ---------------- VARIABILI ----------------
    listaParola = []
    tentativi = []
    maxTentativi = 6
    
    # ---------------- TASTIERA CLICCABILE ----------------
    tasti_mouse = {
        "casa": pygame.Rect(650, 20, 50, 50),
        "retry": pygame.Rect(710, 20, 50, 50),
        # PRIMA RIGA
        "Q": pygame.Rect(67, 510, 65, 70),
        "W": pygame.Rect(138, 510, 65, 70),
        "E": pygame.Rect(210, 510, 60, 70),
        "R": pygame.Rect(275, 510, 60, 70),
        "T": pygame.Rect(345, 510, 60, 70),
        "Y": pygame.Rect(410, 510, 60, 70),
        "U": pygame.Rect(480, 510, 60, 70),
        "I": pygame.Rect(547, 510, 60, 70),
        "O": pygame.Rect(615, 510, 60, 70),
        "P": pygame.Rect(680, 510, 60, 70),
        # SECONDA RIGA
        "A": pygame.Rect(100, 585, 60, 70),
        "S": pygame.Rect(170, 585, 60, 70),
        "D": pygame.Rect(240, 585, 60, 70),
        "F": pygame.Rect(310, 585, 60, 70),
        "G": pygame.Rect(380, 585, 60, 70),
        "H": pygame.Rect(450, 585, 60, 70),
        "J": pygame.Rect(515, 585, 60, 70),
        "K": pygame.Rect(583, 585, 60, 70),
        "L": pygame.Rect(650, 585, 60, 70),
        # TERZA RIGA
        "INVIO": pygame.Rect(70, 660, 95, 70),
        "Z": pygame.Rect(170, 660, 60, 70),
        "X": pygame.Rect(240, 660, 60, 70),
        "C": pygame.Rect(310, 660, 60, 70),
        "V": pygame.Rect(380, 660, 60, 70),
        "B": pygame.Rect(450, 660, 60, 70),
        "N": pygame.Rect(515, 660, 60, 70),
        "M": pygame.Rect(583, 660, 60, 70),
        "CANC": pygame.Rect(650, 660, 95, 70),
    }
    
    # ---------------- TIMER ----------------
    FontTimer = pygame.font.SysFont('Impact', 40)
    tempo_inizio = pygame.time.get_ticks()
    tempoAttuale = 0
    
    runningGioco = True
    while runningGioco:
        # ---------------- DISEGNO TIMER ----------------
        if not giocoFinito:
            tempoAttuale = (pygame.time.get_ticks() - tempo_inizio) // 1000
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runningGioco = False
                pygame.quit()
                return
            
            # ---------------- MOUSE ----------------
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos_mouse = pygame.mouse.get_pos()
                for tasto, rect in tasti_mouse.items():
                    if rect.collidepoint(pos_mouse):
                        if tasto == "INVIO":
                            if giocoFinito:
                                continue
                            parolaInserita = "".join(listaParola)
                            if len(listaParola) == 5 and parolaInserita in paroleAccettabili:
                                tentativi.append(parolaInserita)
                                listaParola = []
                                
                                if parolaInserita == parolaSceltaComputer:
                                    vittoria(nome_giocatore, tempoAttuale)
                                elif len(tentativi) == maxTentativi:
                                    sconfitta()
                        
                        elif tasto == "CANC":
                            if giocoFinito:
                                continue
                            if len(listaParola) > 0:
                                listaParola.pop()
                        
                        elif tasto == "casa":
                            runningGioco = False
                            main()
                            return
                        
                        elif tasto == "retry":
                            runningGioco = False
                            if not parolaSpeciale:
                                parolaSceltaComputer = random.choice(ParoleComputer)
                            gioco(nome_giocatore, parolaSceltaComputer, parolaSpeciale, ParoleComputer)
                            return
                        
                        else:
                            if len(listaParola) < 5:
                                listaParola.append(tasto)
            
            # ---------------- TASTIERA ----------------
            if event.type == pygame.KEYDOWN and not giocoFinito:
                if event.key == pygame.K_ESCAPE:
                    runningGioco = False
                    main()
                    return
                
                elif event.key == pygame.K_BACKSPACE and len(listaParola) > 0:
                    listaParola.pop()
                
                elif event.key == pygame.K_RETURN:
                    parolaInserita = "".join(listaParola)
                    if len(listaParola) == 5 and parolaInserita in paroleAccettabili:
                        tentativi.append(parolaInserita)
                        listaParola = []
                        
                        if parolaInserita == parolaSceltaComputer:
                            vittoria(nome_giocatore, tempoAttuale)
                        elif len(tentativi) == maxTentativi:
                            sconfitta()
                
                else:
                    caratterePremuto = event.unicode.upper()
                    if caratterePremuto in "QWERTYUIOPASDFGHJKLZXCVBNM" and len(listaParola) < 5:
                        listaParola.append(caratterePremuto)
            
            # Permette di rigiocare premendo R dopo la fine della partita
            if event.type == pygame.KEYDOWN and giocoFinito:
                if event.key == pygame.K_r:
                    runningGioco = False
                    if not parolaSpeciale:
                        parolaSceltaComputer = random.choice(ParoleComputer)
                    gioco(nome_giocatore, parolaSceltaComputer, parolaSpeciale, ParoleComputer)
                    return
        
        #mostro lo sfondo
        schermo.blit(imgSfondo, (0, 0))
        schermo.blit(imgCasa, (650, 20))
        schermo.blit(imgRetry, (710, 20))
        
        # Disegno i tentativi colorati
        for riga in range(len(tentativi)):
            parola = tentativi[riga]
            segreta = list(parolaSceltaComputer)
            colori = [""] * 5
            
            # Verde
            for i in range(5):
                if parola[i] == segreta[i]:
                    colori[i] = (0, 200, 0)
                    segreta[i] = ""
            
            # Giallo / Rosso
            for i in range(5):
                if colori[i] == "":
                    if parola[i] in segreta:
                        colori[i] = (220, 200, 0)
                        segreta[segreta.index(parola[i])] = ""
                    else:
                        colori[i] = (200, 0, 0)
            
            # Disegna caselle
            for num in range(5):
                coordinataX = 200 + num * 92
                coordinataY = 20 + riga * 77
                pygame.draw.rect(schermo, colori[num], (coordinataX, coordinataY, 70, 70))
                testo = FontLettere.render(parola[num], True, "black")
                schermo.blit(testo, (coordinataX + 15, coordinataY))
        
        # Disegno la parola in corso
        rigaAttuale = len(tentativi)
        for num in range(len(listaParola)):
            coordinataX = 200 + num * 92
            coordinataY = 20 + rigaAttuale * 77
            pygame.draw.rect(schermo, "white", (coordinataX, coordinataY, 70, 70))
            testo = FontLettere.render(listaParola[num], True, "black")
            schermo.blit(testo, (coordinataX + 15, coordinataY))
        
        # Disegno il timer
        testoTimer = FontTimer.render(f"{tempoAttuale}s", True, (0, 0, 0))
        schermo.blit(testoTimer, (50, 20))
        
        # Aggiorno lo schermo
        pygame.display.flip()
    
#--------------------------------------------------------------------
    
# **funzioni**
#
# Questo modulo contiene tutte le funzioni principali del gioco Insultle.
# Gestisce l'interfaccia grafica, l'inserimento del nome
# del giocatore, il menu iniziale, la logica di gioco ispirata a Wordle,
# il sistema di tentativi, il timer, gli effetti sonori e la visualizzazione
# della classifica. Include inoltre la gestione degli input da tastiera e mouse
# e il caricamento delle risorse (immagini, suoni e file di testo).
#
# License: See LICENSE file in the project root for details.
# 
# autori: Dafne Belardinelli, Edoardo Pani, Qian Qian Zhang
# Dafne Belardinelli: dafne.belardinelli@gmail.com
# Edoardo Pani: edoardorobertopani@gmail.com
# Qian Qian Zhang: zhangqianqian80@gmail.com
