from Modules.Funcions import *
import os
from CliUtils import CliUtils
from Modules.Constants import Actions
"""
Classe di interfaccia con la linea di comando
Si ocupa della stampa dei menu e della gestione delle scelte
"""


"""
Stampa il menù principale e gestisce la scelta relativa
Ritorna la scelta mella classe cli.py.
Tale valore verrà usato per chiamare gli altrimetodi di questa classe
"""
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
"""
Primo metodo di interfaccia del menù principale
Serve per creare un nuovo file vuoto di todos
"""
def crea_file():
    os.system('cls')
    nome_lista = input("Inserisci il nome della lista da creare (o esci per tornare indietro senza creare): ")
    if (nome_lista != 'esci'):
        return_message = crea(nome_lista)
        print(return_message)

"""
Metodo che si occupa della cancellazione di uno dei file di todos dalla memoria
"""
def cancella_file():
    indice = ""
    while indice != 'esci':
        os.system('cls')
        file_list = listFile()
        CliUtils.stampa_lista(file_list)
        print()
        indice = input("Inserisci l'indice dell'elemento da cancellare(o esci per tornare indietro senza cancellare): ")
        if (indice != 'esci'):
            try:
                return_message = cancella(int(indice))
                print(return_message)
                input()
            except ValueError:
                print()
                print("Input non valido inserisci un numero")
                print("-" * 31)
                print()

def esci_programma():
    os.system('cls')
    print("Programma terminato")
"""
Si occupa di gestire un messaggio di errore per i casi non conteplati preceedntemente
"""
def default_case(scelta):
    if scelta != Actions.INPUT_NON_VALIDO:
        print()
        print("Scelta non valida")
    input()



def modifica_file():
    indice = ""
    while indice != 'esci':
        os.system('cls')
        file_list = listFile()
        CliUtils.stampa_lista(file_list)
        print()
        indice = input("Inserisci l'indice dell'elemento da editare(o esci per tornare indietro senza modificare): ")
        if (indice != 'esci'):
            gestisci_edit(indice)


"""
metodo di gestione del primo livello di interfaccia per le operazioni di edit
"""
def gestisci_edit(indice):
    try:
        os.system('cls')
        ret_is_todos = is_todos(int(indice))
        if(ret_is_todos['messages'] is not None):
            os.system('cls')
            print(ret_is_todos["messages"])
            input()
        else:
            if ret_is_todos['esito']:
                scelta_edit = -1
                while scelta_edit != Actions.USCITA:
                    os.system('cls')
                    scelta_edit = CliUtils.stampa_menu_edit()
                    match scelta_edit:
                        case Actions.EDIT_AGGIUNGI:
                            CliUtils.aggiungi_edit(indice)
                        case Actions.EDIT_MODIFICA:
                            CliUtils.modifica_edit(int(indice))
                        case Actions.EDIT_CANCELLA:
                            CliUtils.cancella_edit(int(indice))
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




