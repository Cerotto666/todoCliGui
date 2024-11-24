from GuiUtils import windows as w, actions as a
import PySimpleGUI as sg
from Modules.Constants import Windows_name as wn
from Modules import Funcions as f

def handle_home():
    layout = w.get_layout_home()
    window = sg.Window("Home", layout, finalize=True)
    files = f.listFile(True)
    window['todos'].update(values=files)

    while True:
        print("Main")
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, "Esci"):
            break
        elif event == "CREA":
            a.crea(window)
        elif event == "RINOMINA":
            a.rinomina(window)
        elif event == "CANCELLA":
            a.cancella(window)
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
    print("Visualizza")
    layout = w.get_layout_visualizza()
    window = sg.Window("Visualizza", layout, finalize=True)
    files = f.listFile(True)
    todos = []
    window['visualizza_file'].update(values=files)

    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, "Esci"):
            break
        elif event == "visualizza_file":
            file_to_visualize = values['visualizza_file'][0]
            todos = f.get_todos_file(file_to_visualize)
            dones = f.get_dones_file(file_to_visualize)
            window['visualizza_todos'].update(values=todos)
            window['visualizza_done'].update(values=dones)
        elif event == "INDIETRO":
            window.close()
            return wn.HOME

    window.close()
    return None