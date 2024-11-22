
import os
from Modules import Constants


def listFile(gui=False):
    file_list = []
    for index, file_path in enumerate(Constants.directory.iterdir()):
        if file_path.is_file() and file_path.suffix == ".txt":
            if gui:
                file_list.append(file_path.name)
            else:
                file_list.append(str(index + 1) + ") - " +file_path.name)
    return file_list


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


def crea(filename):
    file_path = Constants.directory / f"{filename}.txt"
    file_path.touch(exist_ok=True)
    return f"File creato: {file_path}"


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


def save_todos(indice, todos):
    lista_file = [file.name for file in Constants.directory.iterdir() if file.is_file()]
    file_path = Constants.directory / f"{lista_file[indice - 1]}"
    with file_path.open("w") as file:
        file.write("\n".join(todos))


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
    
