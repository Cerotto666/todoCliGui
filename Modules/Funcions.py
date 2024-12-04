import PySimpleGUI as sg
from Modules import Constants
import os
import sys


def listFile(gui=False):
    file_list = []
    for index, file_path in enumerate(Constants.directory.iterdir()):
        if file_path.is_file() and file_path.suffix == ".txt":
            if gui:
                file_list.append(file_path.stem)
            else:
                file_list.append(str(index + 1) + ") - " +file_path.name)
    return file_list


def cancella_file(filename):
    file_path = Constants.directory / f"{filename}.txt"
    file_path_dones = Constants.direcotry_done / f"{filename}_done.txt"
    if file_path.exists():
        file_path.unlink()
    if file_path_dones.exists():
        file_path_dones.unlink()

def cancella(indice):
    lista_file = [file.name for file in Constants.directory.iterdir() if file.is_file()]
    try:
        file_path = Constants.directory / f"{lista_file[indice-1]}"
        if file_path.exists():
            file_path.unlink()
            return f"File '{file_path}' cancellato."
        else:
            return f"File '{file_path}' non esiste."
    except IndexError:
        ret_mes = ("-" * 31 + "\n") + "L'elemento non esiste"
        return ret_mes


def init():
    if not Constants.directory.exists():
        Constants.directory.mkdir(parents=True)
    if not Constants.direcotry_done.exists():
        Constants.direcotry_done.mkdir()


def crea(filename):
    file_path = Constants.directory / f"{filename}.txt"
    file_path_done = Constants.direcotry_done / f"{filename}_done.txt"
    if not file_path.exists():
        file_path.touch(exist_ok=True)
        file_path_done.touch(exist_ok=True)
        return f"File creato: {file_path}"
    else:
        return "NO"

def sovrascrivi(filename):
    file_path = Constants.directory / f"{filename}.txt"
    file_path.write_text("")


def is_todos(indice):
    return_state = {}
    lista_file = [file.name for file in Constants.directory.iterdir() if file.is_file()]
    try:
        file_path = Constants.directory / f"{lista_file[indice - 1]}"
        if file_path.exists():
            return_state['messages'] = None
            return_state['esito'] = True
            return return_state
        else:
            return_state['messages'] = None
            return_state['esito'] = False
            return return_state
    except IndexError:
        return_state['messages'] = "L'elemento non esiste \n" + "-" * 31
        return_state['esito'] = False
        return return_state


def get_todos(indice):
    lista_file = [file.name for file in Constants.directory.iterdir() if file.is_file()]
    file_path = Constants.directory / f"{lista_file[indice - 1]}"
    righe = list(file_path.read_text().splitlines())
    return righe

def get_todos_file(file):
    file_path = Constants.directory / f"{file}.txt"
    righe = list(file_path.read_text().splitlines())
    return righe

def get_dones_file(file):
    file_path = Constants.direcotry_done / f"{file}_done.txt"
    righe = list(file_path.read_text().splitlines())
    return righe

def save_todos(indice, todos):
    lista_file = [file.name for file in Constants.directory.iterdir() if file.is_file()]
    file_path = Constants.directory / f"{lista_file[indice - 1]}"
    with file_path.open("w") as file:
        file.write("\n".join(todos))

def save_files(todos, dones, file_name):
    file_path_todos = Constants.directory / f"{file_name}.txt"
    file_path_dones = Constants.direcotry_done / f"{file_name}_done.txt"
    with file_path_todos.open("w") as file:
        file.write("\n".join(todos))
    with file_path_dones.open("w") as file:
        file.write("\n".join(dones))

def save_file(list_to_save, file_name, is_todos):
    if is_todos:
        file_path_todos = Constants.directory / f"{file_name}.txt"
        with file_path_todos.open("w") as file:
            file.write("\n".join(list_to_save))
    else:
        file_path_dones = Constants.direcotry_done / f"{file_name}_done.txt"
        with file_path_dones.open("w") as file:
            file.write("\n".join(list_to_save))


def aggiungi_todo(indice, new_todo):
    os.system("cls")
    todos = get_todos(int(indice))
    todos.append(new_todo)
    save_todos(int(indice), todos)


def modifica_file(todos, new_todo, modifica_indice, indice):
    todos[int(modifica_indice) - 1] = new_todo
    save_todos(int(indice), todos)


def elimina_todo(todos, elimina_indice, indice):
    todos.pop(int(elimina_indice) - 1)
    save_todos(int(indice), todos)

def rename(old_name, new_name):
    new_file_path = Constants.directory / f"{new_name}.txt"
    old_file_path = Constants.directory / f"{old_name}.txt"
    new_file_path_dones = Constants.direcotry_done / f"{new_name}_done.txt"
    old_file_path_dones = Constants.direcotry_done / f"{old_name}_done.txt"
    if new_file_path.exists():
            raise FileExistsError(f"Il file '{new_file_path}' esiste già.")
    if not old_file_path.exists():
        raise  FileNotFoundError(f"Il file '{old_file_path}' non esiste")
    old_file_path.rename(new_file_path)
    old_file_path_dones.rename(new_file_path_dones)
    
def init_gui():

    init()
    sg.theme("DarkBlue14")
    lista_file = [file.stem for file in Constants.directory.iterdir() if file.is_file()]
    for file in lista_file:
        done_file = Constants.direcotry_done / f"{file}_done.txt"
        if not done_file.exists():
            done_file.touch(exist_ok=True)
    return Constants.Windows_name.HOME

def get_base_path():
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, "Images\\bye.png")
    else:
        return os.path.join(os.path.abspath("."), "Images\\bye.png")




