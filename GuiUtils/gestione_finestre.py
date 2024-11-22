from GuiUtils import windows as w
import PySimpleGUI as sg
from Modules.Constants import Windows_name as wn
from Modules import Funcions as f

def handle_home():
    layout = w.get_layout_home()
    window = sg.Window("Home", layout, finalize=True)
    files = f.listFile(True)
    window['todos'].update(values=files)

    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, "Esci"):
            break
        elif event == "RINOMINA":
            print("rinomina")
        elif event == "CREA":
            print("crea")
        elif event == "CANCELLA":
            print("Cancella")
        elif event == "MODIFICA":
            window.close()
            return wn.MODIFICA
        elif event == "VISUALIZZA":
            window.close()
            return wn.VISUALIZZA

    window.close()
    return None

def handle_modifica():
    layout = w.get_layout_modifica()
    window = sg.Window("Modifica", layout)

    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, "Esci"):
            break
        elif event == "HOME":
            window.close()
            return wn.HOME

    window.close()
    return None


def handle_visualizza():
    layout = w.get_layout_visualizza()
    window = sg.Window("Visualizza", layout)

    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, "Esci"):
            break
        elif event == "HOME":
            window.close()
            return wn.HOME

    window.close()
    return None