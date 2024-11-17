from Modules.Funcions import *
import os
from Modules.Actions import Actions

def stampa_menu():
    init()
    os.system('cls')
    print("-" * 31)
    print("1) Crea una nuova lista")
    print("2) Cancella una lista esistente")
    print("3) Modifica una lista esistente")
    print("0) Esci")
    print("-" * 31)
    print()

    try:
        scelta = int(input("Fai la tua scelta: "))
    except ValueError:
        print()
        print("Input non valido inserisci un numero")
        scelta = -1

    return scelta

def crea_file():
    os.system('cls')
    nome_lista = input("Inserisci il nome della lista da creare (o esci per tornare indietro senza creare): ")
    if (nome_lista != 'esci'):
        crea(nome_lista)

def cancella_file():
    os.system('cls')
    listFile()
    print()
    indice = ""
    while indice != 'esci':
        indice = input("Inserisci l'indice dell'elemento da cancellare(o esci per tornare indietro senza cancellare): ")
        if (indice != 'esci'):
            try:
                cancella(int(indice))
            except ValueError:
                print()
                print("Input non valido inserisci un numero")
                print("-" * 31)
                print()

def esci_programma():
    os.system('cls')
    print("Programma terminato")

def default_case(scelta):
    if scelta != Actions.INPUT_NON_VALIDO:
        print()
        print("Scelta non valida")
    input()

def modifica_file():

    indice = ""
    while indice != 'esci':
        os.system('cls')
        listFile()
        print()
        indice = input("Inserisci l'indice dell'elemento da editare(o esci per tornare indietro senza modificare): ")
        if (indice != 'esci'):
            gestisci_edit(indice)



def gestisci_edit(indice):
    try:
        os.system('cls')
        if is_todos(int(indice)):
            scelta_edit = -1
            while scelta_edit != Actions.USCITA:
                os.system('cls')
                scelta_edit = stampa_menu_edit()
                match scelta_edit:
                    case Actions.EDIT_AGGIUNGI:
                        aggiungi_edit(indice)
                    case Actions.EDIT_MODIFICA:
                        modifica_edit(int(indice))
                    case Actions.EDIT_CANCELLA:
                       cancella_edit(int(indice))
                    case Actions.USCITA:
                        print()
                    case _:
                        if scelta_edit != Actions.INPUT_NON_VALIDO:
                            print()
                            print("Scelta non valida")
                        input()
    except ValueError:
        print()
        print("Input non valido inserisci un numero")
        print("-" * 31)
        print()
        input()

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
        scelta_edit = Actions.INPUT_NON_VALIDO
    return scelta_edit
