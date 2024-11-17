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
    os.system('cls')
    listFile()
    print()
    indice = ""
    while indice != 'esci':
        indice = input("Inserisci l'indice dell'elemento da editare(o esci per tornare indietro senza modificare): ")
        if (indice != 'esci'):
            gestisci_edit(indice)



def gestisci_edit(indice):
    try:
        mostra_todos(int(indice))
    except ValueError:
        print()
        print("Input non valido inserisci un numero")
        print("-" * 31)
        print()