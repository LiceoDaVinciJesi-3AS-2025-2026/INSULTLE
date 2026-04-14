from importlib.resources import files
from pathlib import Path

# eventualmente aggiungere tutte le funzioni relative alle cartelle che avete creato in src.
def get_sound(filename: str) -> Path:
    return files(__package__) / "suoni" / filename

def get_image(filename: str) -> Path:
    return files(__package__) / "immagini" / filename

def get_data(filename: str) -> Path:
    return files(__package__) / filename