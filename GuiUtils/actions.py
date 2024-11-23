from Modules import Funcions as f
import PySimpleGUI as sg
from GuiUtils import window_status as ws

def crea(window):

    ws.init_crea(window)
    is_clear = True
    
    while is_clear:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, "Esci"):
            is_clear = False
        elif event == "OK":
            nuovo_file = values['todo']
            if nuovo_file != "":
                creato = f.crea(nuovo_file)
                if creato == "NO":
                    response = sg.popup_yes_no("Vuoi sovrascrivere?")
                    if response == "Yes":
                        f.sovrascrivi(nuovo_file)
                        is_clear = False
                else:
                    is_clear = False
            else:
                sg.popup_ok("Il nome file non può essere vuoto")
        elif event == "CANCELLA":
            is_clear = False
                
    ws.exit_crea(window)

