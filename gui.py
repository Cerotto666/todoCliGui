
from Modules.Constants import Windows_name as wn
from GuiUtils import windows, gestione_finestre as gf
from Modules import Funcions as f

current_window = f.init_gui()
file_name = ""

while current_window:
    if current_window == wn.HOME:
        current_window = gf.handle_home()
    elif current_window == wn.MODIFICA:
        current_window = gf.handle_modifica()
    elif current_window == wn.VISUALIZZA:
        current_window = gf.handle_visualizza()

gf.handle_bye()