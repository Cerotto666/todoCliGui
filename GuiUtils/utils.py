import PySimpleGUI as sg
from PIL import Image, ImageTk
import io

def resize_image(size, base_path):
    """
    Ridimensiona un'immagine e la restituisce in formato compatibile con PySimpleGUI.
    :param path: Percorso dell'immagine
    :param size: Dimensioni desiderate (larghezza, altezza)
    :return: Oggetto immagine compatibile con PySimpleGUI
    """
    print(base_path)
    image = Image.open(base_path)
    image = image.resize(size, Image.Resampling.LANCZOS)  # Ridimensiona l'immagine mantenendo la qualità
    bio = io.BytesIO()
    image.save(bio, format="PNG")
    del image
    return bio.getvalue()