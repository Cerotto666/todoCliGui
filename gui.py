import PySimpleGUI as sg
import os
import sys
from Modules.Constants import Windows_name as wn
from GuiUtils import windows, gestione_finestre as gf

# Gestione del percorso in base all'ambiente (sviluppo o eseguibile)
if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS  # Percorso temporaneo nell'eseguibile
else:
    base_path = os.path.dirname(__file__)

sg.theme("DarkBlue14")
layout = windows.get_layout_home()
window = sg.Window("Gestione Layout", layout)
current_window = wn.HOME

while current_window:
    if current_window == wn.HOME:
        current_window = gf.handle_home()
    elif current_window == wn.MODIFICA:
        current_window = gf.handle_modifica()
    elif current_window == wn.VISUALIZZA:
        current_window = gf.handle_visualizza()


layout = windows.get_layout_bye()
window = sg.Window("BYE", layout, element_justification="center", finalize=True)
window.read()
window.close()