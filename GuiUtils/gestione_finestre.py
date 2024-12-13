from GuiUtils import windows as w, actions as a
import PySimpleGUI as sg
from Modules.Constants import Windows_name as wn
from Modules import Funcions as f

def handle_home(parent_window_location):
    parent_x, parent_y = parent_window_location
    new_window_x = parent_x + 50
    new_window_y = parent_y + 50
    layout = w.get_layout_home()
    window = sg.Window("Home", layout, finalize=True, location=(new_window_x, new_window_y))
    files = f.listFile(True)
    window['todos'].update(values=files)
    current_location = window.CurrentLocation()
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
                return wn.MODIFICA, current_location
            else:
                sg.popup_ok("Devi prima selezionare un file")
        elif event == "VISUALIZZA":
            current_location = window.CurrentLocation()
            window.close()
            return wn.VISUALIZZA, current_location

    current_location = window.CurrentLocation()
    window.close()
    return None, current_location

def handle_modifica(parent_window_location):
    parent_x, parent_y = parent_window_location
    new_window_x = parent_x + 50
    new_window_y = parent_y + 50
    layout = w.get_layout_modifica()
    window = sg.Window("Modifica", layout, finalize=True, location=(new_window_x, new_window_y))
    global file_name
    a.init_modifica(window, file_name)
    selected_element = ""
    current_location = window.CurrentLocation()

    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, "Esci"):
            break
        elif event in ("visualizza_todos_modifica", "visualizza_dones_modifica"):
            selected_element = a.text_clicked(window, event, values)
        elif event == "mark_as":
            a.mark_as(window, file_name, selected_element)
            a.reset_modifica(window)
        elif event == "modifica_modifica":
            a.modifica_elemento(window, file_name, selected_element, values, True)
            a.reset_modifica(window)
        elif event == "cancella_modifica":
            a.modifica_elemento(window, file_name, selected_element, values, False)
            a.reset_modifica(window)
        elif event == "aggiungi_modifica":
            if a.aggiungi_modifica(window, file_name, values):
                a.reset_modifica(window)
        elif event == "indietro_modifica":
            current_location = window.CurrentLocation()
            window.close()
            return wn.HOME, current_location
    current_location = window.CurrentLocation()
    window.close()
    return None, current_location


def handle_visualizza(parent_window_location):
    parent_x, parent_y = parent_window_location
    new_window_x = parent_x + 50
    new_window_y = parent_y + 50
    print("Visualizza")
    layout = w.get_layout_visualizza()
    window = sg.Window("Visualizza", layout, finalize=True, location=(new_window_x, new_window_y))
    files = f.listFile(True)
    window['visualizza_file'].update(values=files)
    current_location = window.CurrentLocation()

    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, "Esci"):
            break
        elif event == "visualizza_file":
            a.visualizza(window, values)
        elif event == "INDIETRO":
            current_location = window.CurrentLocation()
            window.close()
            return wn.HOME, current_location

    current_location = window.CurrentLocation()
    window.close()
    return None, current_location

def handle_bye(base_path):
    layout = w.get_layout_bye(base_path)
    window = sg.Window("BYE", layout, element_justification="center", finalize=True)
    window.read()
    window.close()