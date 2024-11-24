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

def rinomina(window):

    ws.init_rinomina(window)
    is_clear = True
    file_to_rename = ""
    while is_clear:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, "Esci"):
            is_clear = False
        elif event == "CANCELLA":
            is_clear = False
        elif event == "todos":
            file_to_rename = values['todos'][0]
            window['OK'].update(disabled=False)
            window['todo'].update(disabled=False, value=file_to_rename)
        elif event == "OK":
            if values['todo'] != "":
                new_name = values['todo']
                try:
                    f.rename(file_to_rename, new_name)
                    is_clear = False
                except FileNotFoundError:
                    sg.popup_ok("Il file che vuoi modificare non esiste")
                except FileExistsError:
                    sg.popup_ok("Stai sovrascrivendo un file")
            else:
                sg.popup_ok("Il nome file non può essere vuoto")
    ws.exit_rinomina(window)

def cancella(window):
    ws.init_cancella(window)
    is_clear = True
    file_to_delete = ""

    while is_clear:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, "Esci"):
            is_clear = False
        elif event == "CANCELLA":
            is_clear = False
        elif event == "todos":
            file_to_delete = values['todos'][0]
            window['OK'].update(disabled=False)
            window['todo'].update(value=file_to_delete)
        elif event == "OK":
            if file_to_delete != "":
                f.cancella_file(file_to_delete)
            is_clear = False

    ws.exit_cancella(window)

