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

def visualizza(window, values):
    file_to_visualize = values['visualizza_file'][0]
    todos = f.get_todos_file(file_to_visualize)
    dones = f.get_dones_file(file_to_visualize)
    window['visualizza_todos'].update(values=todos)
    window['visualizza_done'].update(values=dones)

def init_modifica(window, filename):
    todos = f.get_todos_file(filename)
    dones = f.get_dones_file(filename)
    window['visualizza_todos_modifica'].update(values=todos)
    window['visualizza_dones_modifica'].update(values=dones)

def text_clicked(window, event, values):
    window['modifica_modifica'].update(disabled=False)
    window['cancella_modifica'].update(disabled=False)
    window['aggiungi_modifica'].update(text="ANNULLA")
    window['todo_to_edit'].update(disabled=False)
    if event == "visualizza_todos_modifica":
        window['mark_as'].update(text="MARK AS DONE", disabled=False)
        todo_to_edit = values['visualizza_todos_modifica'][0]
        window['todo_to_edit'].update(value=todo_to_edit)
        window['visualizza_dones_modifica'].update(set_to_index=[])
    else:
        window['mark_as'].update(text="MARK AS TODO", disabled=False)
        todo_to_edit = values['visualizza_dones_modifica'][0]
        window['todo_to_edit'].update(value=todo_to_edit)
        window['visualizza_todos_modifica'].update(set_to_index=[])
    return todo_to_edit

def mark_as(window, file_name, selected_element):
    if window['mark_as'].ButtonText == "MARK AS DONE":
        todos = f.get_todos_file(file_name)
        todos.remove(selected_element)
        dones = f.get_dones_file(file_name)
        dones.append(selected_element)
        window['visualizza_todos_modifica'].update(values=todos)
        window['visualizza_dones_modifica'].update(values=dones)
    else:
        todos = f.get_todos_file(file_name)
        todos.append(selected_element)
        dones = f.get_dones_file(file_name)
        dones.remove(selected_element)
        window['visualizza_todos_modifica'].update(values=todos)
        window['visualizza_dones_modifica'].update(values=dones)
    f.save_files(todos, dones, file_name)

def reset_modifica(window):
    window['modifica_modifica'].update(disabled=True)
    window['cancella_modifica'].update(disabled=True)
    window['todo_to_edit'].update(disabled=True, value = "")
    window['mark_as'].update(text="MARK AS", disabled=True)
    window['visualizza_todos_modifica'].update(set_to_index=[])
    window['visualizza_dones_modifica'].update(set_to_index=[])

def modifica_elemento(window, file_name, selected_element, values, is_modifica):
    if window['mark_as'].ButtonText == "MARK AS DONE":
        todos = f.get_todos_file(file_name)
        new_todos = values['todo_to_edit']
        if is_modifica:
            index = todos.index(selected_element)
            if new_todos != "":
                todos[index] = new_todos
            else:
                sg.popup_ok("Il nome dell'elemento non può essere vuoto")
        else:
            todos.remove(new_todos)
        f.save_file(todos, file_name, True)
        window['visualizza_todos_modifica'].update(values=todos)
    else:
        dones = f.get_dones_file(file_name)
        new_dones = values['todo_to_edit']
        if is_modifica:
            index = dones.index(selected_element)
            if new_dones != "":
                dones[index] = new_dones
            else:
                sg.popup_ok("Il nome dell'elemento non può essere vuoto")
        else:
            dones.remove(new_dones)
        window['visualizza_dones_modifica'].update(values=dones)
        f.save_file(dones, file_name, False)

def aggiungi_modifica(window, file_name, values):
    if window['aggiungi_modifica'].ButtonText == "AGGIUNGI":
        window['todo_to_edit'].update(disabled=False, value="")
        window['aggiungi_modifica'].update(text="OK")
        return False
    elif window['aggiungi_modifica'].ButtonText == "ANNULLA":
        window['aggiungi_modifica'].update(text="AGGIUNGI")
        return True
    else:
        window['todo_to_edit'].update(disabled=True, value="")
        window['aggiungi_modifica'].update(text="AGGIUNGI")
        if values['todo_to_edit'] != "":
            todos = f.get_todos_file(file_name)
            new_todos = values['todo_to_edit']
            todos.append(new_todos)
            f.save_file(todos, file_name, True)
            window['visualizza_todos_modifica'].update(values=todos)
        else:
            sg.popup_ok("Il testo non può essere vuoto")
    return True







