import PySimpleGUI as sg
import os
import sys
from Modules.Constants import Windows_name as wn
from GuiUtils import windows

# Gestione del percorso in base all'ambiente (sviluppo o eseguibile)
if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS  # Percorso temporaneo nell'eseguibile
else:
    base_path = os.path.dirname(__file__)

sg.theme("DarkBlue14")
layout = windows.get_layout_home()
window = sg.Window("Gestione Layout", layout)
current_layout = wn.HOME

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WINDOW_CLOSED or event == "Esci" or event == "Chiudi":
        break

    if event == "CREA":
        window.close()
        layout = windows.get_layout_crea()
        window = sg.Window("Finestra Crea", layout)
        current_layout = wn.CREA

    elif event == "HOME":
        window.close()
        layout = windows.get_layout_home()
        window = sg.Window("Finestra Home", layout)
        current_layout = wn.HOME

    elif event == "MODIFICA":
        window.close()
        layout = windows.get_layout_modifica()
        window = sg.Window("Finestra Modifica", layout)
        current_layout = wn.MODIFICA

    elif event == "VISUALIZZA":
        window.close()
        layout = windows.get_layout_visualizza()
        window = sg.Window("Finestra Visualizza", layout)
        current_layout = wn.VISUALIZZA

    elif event == "CANCELLA":
        window.close()
        layout = windows.get_layout_cancella()
        window = sg.Window("Finestra Cancella", layout)
        current_layout = wn.CANCELLA


window.close()

"""
current_window = wn.HOME
while True:
    if current_window == wn.HOME:
        window = sg.Window("Home", windows.layout_home)
    elif current_window == wn.CREA:
        window = sg.Window("Crea", windows.layout_crea)
    elif current_window == wn.MODIFICA:
        window = sg.window("Modifica", windows.layout_modifica)
    elif current_window == wn.VISUALIZZA:
        window = sg.window("Visualizza", windows.layout_visualizza)
    elif current_window == wn.CANCELLA:
        window = sg.window("Cancella", windows.layout_cancella)
"""

