# INSULTLE
# Dafne Belardinelli, Edoardo Pani, Qian Qian Zhang
from insultle.funzioni import *

#----------------------------------------------------------------------------------

if __name__ == "__main__":
    main() #avvia la schermata iniziale
    #pygame.quit() #chiude Pygame quando il gioco termina

# **Insultle** 
# è un gioco ispirato a Wordle, il cui l'obiettivo è indovinare una parola segreta di 5 lettere, ma… tutte le parole sono "insulti".
# ovviamente avrai degli indizi, per ogni tentativo ti faremmo sapere se ogni lettere di tale parola è assente o presente, nella giusta posizione o meno.
# 
# Il gioco chiama la funzione main(), cioè la schermata iniziale, da quì il codice si biforca in: modalità classsica e nella parola del giorno.
# Entrambe richiamano la funzione nome(), quest'ultima chiedere un nome nickname all'utente (per una prossima classifica).
# Dopodichè, con la conferma del nome inizia il gioco e anche il timer.
# Indipendentemente da quale modalità si scelga, in caso di vittoria o di sconfitta il gioco mette il suono associato.
# Infine, l'utente può scegliere di tornare alla schermata iniziale o di iniziare un'altra partita all'instante
# 
# License: See LICENSE file in the project root for details.
# 
# autori: Dafne Belardinelli, Edoardo Pani, Qian Qian Zhang
# Dafne Belardinelli: dafne.belardinelli@gmail.com
# Edoardo Pani: edoardorobertopani@gmail.com
# Qian Qian Zhang: zhangqianqian80@gmail.com
