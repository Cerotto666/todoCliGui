import os
from Modules import Funcions, Constants

"""
Metodi per un lauer intermedio tra l'interfacia della cli
e le funzioni generali per le operazioni I/O
"""

def stampa_lista(lista):
    for l in lista:
        print(l)

"""
Il metodo estrae il file_path della lista interessata in base all'indice
"""
def mostra_todos(indice):
    lista_file = [file.name for file in Constants.directory.iterdir() if file.is_file()]
    file_path = Constants.directory / f"{lista_file[indice-1]}"
    if file_path.exists():
        print_todos(file_path)
    return True
"""
Stampa la lista dei todos in base al path del file corrispondente
"""
def print_todos(file_path):
    os.system('cls')
    righe = file_path.read_text().splitlines()
    for index, riga in enumerate(righe):
        print(str(index + 1) + ") " + riga)
    print("-" * 50)
    print()
"""
metodo di gestione del secondo livello di interfaccia per le operazioni di edit
"""
def modifica_edit(indice):
    errore = True
    while errore:
        try:
            errore = False
            mostra_todos(int(indice))
            todos = Funcions.get_todos(int(indice))
            modifica_indice = input("Quale todo vuoi modificare (esci per uscire): ")
            if modifica_indice != 'esci':
                todos[int(modifica_indice) - 1] = ""
            print()
            if (modifica_indice != 'esci'):
                new_todo = input("Inserisci todo modificato: ")
                Funcions.modifica_file(todos, new_todo, modifica_indice, indice)
        except ValueError:
            print("Inserisci un valore numerico")
            errore = True
            input()
        except IndexError:
            print("Elemento non presente")
            errore = True
            input()
"""
metodo di gestione del secondo livello di interfaccia per le operazioni di edit
"""
def cancella_edit(indice):
    errore = True
    while errore:
        try:
            errore = False
            mostra_todos(int(indice))
            todos = Funcions.get_todos(int(indice))
            elimina_indice = input("Quale todo vuoi cancellare (esci per uscire): ")
            if elimina_indice != 'esci':
                todos[int(elimina_indice) - 1] = ""
            print()
            if (elimina_indice != 'esci'):
                Funcions.elimina_todo(todos, elimina_indice, indice)
        except ValueError:
            print("Inserisci un valore numerico")
            errore = True
            input()
        except IndexError:
            print("Elemento non presente")
            errore = True
            input()

"""
metodo di gestione del secondo livello di interfaccia per le operazioni di edit
"""
def aggiungi_edit(indice):
    new_todo = input("Inserisci todo: ")
    Funcions.aggiungi_todo(indice, new_todo)

"""
Stampa e gestione della scelta per il secondo livello di interfaccia
"""
def stampa_menu_edit():
    print("-" * 31)
    print("1) Aggiungi todo")
    print("2) Modifica todo")
    print("3) Cancella todo")
    print("0) Esci")
    print("-" * 31)
    print()
    try:
        scelta_edit = int(input("Fai la tua scelta: "))
    except ValueError:
        print()
        print("Input non valido inserisci un numero")
        print()
        scelta_edit = Constants.INPUT_NON_VALIDO
    return scelta_edit