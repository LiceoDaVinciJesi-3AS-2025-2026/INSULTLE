from importlib.resources import files
from pathlib import Path

# eventualmente aggiungere tutte le funzioni relative alle cartelle che avete creato in src.
def get_sound(filename: str) -> Path:
    return files(__package__) / "suoni" / filename

def get_image(filename: str) -> Path:
    return files(__package__) / "immagini" / filename

def get_data(filename: str) -> Path:
    return files(__package__) / filename

# **resources**
#
# Questo modulo fornisce utility per recuperare percorsi di file
# all'interno del pacchetto, come suoni, immagini e altri dati,
# utilizzando importlib.resources in modo portabile.
# 
# License: See LICENSE file in the project root for details.
# 
# autori: Dafne Belardinelli, Edoardo Pani, Qian Qian Zhang
# Dafne Belardinelli: dafne.belardinelli@gmail.com
# Edoardo Pani: edoardorobertopani@gmail.com
# Qian Qian Zhang: zhangqianqian80@gmail.com
