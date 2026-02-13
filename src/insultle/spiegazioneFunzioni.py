#file spiegazioni

import pygame

if event.type == pygame.KEYDOWN: #quando si preme un tasto, l'azione diventa un evento, gli eventi posso fornire diverse informazioni come che
                                 #il codice del tasto premuto (event.code)
    lettera_premuta = event.unicode #unicode invece associa quel codice a un tasto vero e proprio, tendendo in considerazione anche
                                    #lo SHIFT

testoResoImg = FontLettere.render(f"{letteraPremuta.upper()}", True, "black") #renderizza una str in una img (in python si dice surface)
                                  #text : una stringa                         #fondamentale perchè screen.blit aggiunge allo schermo unicamente
                                  #booleano : True --> testo morbido          #img e non scritte
                                  #           False --> testo con i pixel
                                  #colore: come stringa
                                  #background : opzionale (come se la scritta fosse evidenziata)