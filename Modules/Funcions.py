from pathlib import Path
import os

directory = Path("./Files")
def listFile():
    for index, file_path in enumerate(directory.iterdir()):
        if file_path.is_file() and file_path.suffix == ".txt":
            print(str(index + 1) + ") - " +file_path.name)

def cancella(indice):
    lista_file = [file.name for file in directory.iterdir() if file.is_file()]
    try:
        file_path = directory / f"{lista_file[indice-1]}"
        if file_path.exists():
            file_path.unlink()
            print(f"File '{file_path}' cancellato.")
        else:
            print(f"File '{file_path}' non esiste.")
        input()
    except IndexError:
        print("-" * 31)
        print("L'elemento non esiste")
        input()


def init():
    if not directory.exists():
        directory.mkdir(parents=True)

def crea(filename):
    file_path = directory / f"{filename}.txt"
    file_path.touch(exist_ok=True)
    print(f"File creato: {file_path}")

def mostra_todos(indice):
    lista_file = [file.name for file in directory.iterdir() if file.is_file()]
    file_path = directory / f"{lista_file[indice-1]}"
    if file_path.exists():
        print_todos(file_path)
    return True


def is_todos(indice):
    lista_file = [file.name for file in directory.iterdir() if file.is_file()]
    try:
        file_path = directory / f"{lista_file[indice - 1]}"
        if file_path.exists():
            return True
        else:
            return False
    except IndexError:
        os.system('cls')
        print("L'elemento non esiste")
        print("-" * 31)
        input()
        return False

def print_todos(file_path):
    os.system('cls')
    righe = file_path.read_text().splitlines()
    for index, riga in enumerate(righe):
        print(str(index + 1) + ") " + riga)
    print("-" * 50)
    print()

def get_todos(indice):
    lista_file = [file.name for file in directory.iterdir() if file.is_file()]
    file_path = directory / f"{lista_file[indice - 1]}"
    righe = list(file_path.read_text().splitlines())
    return righe

def save_todos(indice, todos):
    lista_file = [file.name for file in directory.iterdir() if file.is_file()]
    file_path = directory / f"{lista_file[indice - 1]}"
    with file_path.open("w") as file:
        file.write("\n".join(todos))

def aggiungi_edit(indice):
    os.system("cls")
    todos = get_todos(int(indice))
    new_todo = input("Inserisci todo: ")
    todos.append(new_todo)
    save_todos(int(indice), todos)

def modifica_edit(indice):
    errore = True
    while errore:
        try:
            errore = False
            mostra_todos(int(indice))
            todos = get_todos(int(indice))
            modifica_indice = input("Quale todo vuoi modificare (esci per uscire): ")
            if modifica_indice != 'esci':
                todos[int(modifica_indice) - 1] = ""
            print()
            if (modifica_indice != 'esci'):
                new_todo = input("Inserisci todo modificato: ")
                todos[int(modifica_indice) - 1] = new_todo
                save_todos(int(indice), todos)
        except ValueError:
            print("Inserisci un valore numerico")
            errore = True
            input()
        except IndexError:
            print("Elemento non presente")
            errore = True
            input()

def cancella_edit(indice):
    errore = True
    while errore:
        try:
            errore = False
            mostra_todos(int(indice))
            todos = get_todos(int(indice))
            elimina_indice = input("Quale todo vuoi cancellare (esci per uscire): ")
            if elimina_indice != 'esci':
                todos[int(elimina_indice) - 1] = ""
            print()
            if (elimina_indice != 'esci'):
                todos.pop(int(elimina_indice) - 1)
                save_todos(int(indice), todos)
        except ValueError:
            print("Inserisci un valore numerico")
            errore = True
            input()
        except IndexError:
            print("Elemento non presente")
            errore = True
            input()