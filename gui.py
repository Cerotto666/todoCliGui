"""
MAin ->
    GestioneFinestre ->
        Windows(Layouts)
        Actons(Gestione eventi) ->
            WindowStatus (Init ed Exit del layout per ogni azione)

"""
from Modules.Constants import Windows_name as wn
from GuiUtils import gestione_finestre as gf
from Modules import Funcions as f

file_name = ""
current_window = f.init_gui()

while current_window:
    if current_window == wn.HOME:
        current_window = gf.handle_home()
    elif current_window == wn.MODIFICA:
        current_window = gf.handle_modifica()
    elif current_window == wn.VISUALIZZA:
        current_window = gf.handle_visualizza()

gf.handle_bye(f.get_base_path())