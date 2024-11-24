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
            if len(values['todos']) > 0:
                window.close()
                global file_name
                file_name =  values['todos'][0]
                return wn.MODIFICA
            else:
                sg.popup_ok("Devi prima selezionare un file")
        elif event == "VISUALIZZA":
            window.close()
            return wn.VISUALIZZA

    window.close()
    return None

def handle_modifica():
    layout = w.get_layout_modifica()
    window = sg.Window("Modifica", layout, finalize=True)
    global file_name
    a.init_modifica(window, file_name)

    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, "Esci"):
            break
        elif event in ("visualizza_todos_modifica", "visualizza_dones_modifica"):
            a.text_clicked(window, event, values)
        elif event == "mark_as":
            if window['mark_as'].ButtonText == "MARK AS DONE":
                print("MARK AS DONE")
            else:
                print("MARK AS TODO")
        elif event == "indietro_modifica":
            window.close()
            return wn.HOME

    window.close()
    return None


def handle_visualizza():
    print("Visualizza")
    layout = w.get_layout_visualizza()
    window = sg.Window("Visualizza", layout, finalize=True)
    files = f.listFile(True)
    window['visualizza_file'].update(values=files)

    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, "Esci"):
            break
        elif event == "visualizza_file":
            a.visualizza(window, values)
        elif event == "INDIETRO":
            window.close()
            return wn.HOME

    window.close()
    return None

def handle_bye():
    layout = w.get_layout_bye()
    window = sg.Window("BYE", layout, element_justification="center", finalize=True)
    window.read()
    window.close()