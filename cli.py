from Modules.Actions import Actions
from Modules.Funcions import *
import os

scelta = -1

while(scelta != Actions.USCITA):
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
        print("Input non valido inserisci un numero")

    match scelta:
        case Actions.CREA:
            os.system('cls')
            nome_lista = input("Inserisci il nome della lista da creare (o esci per tornare indietro senza creare): ")
            if(nome_lista != 'esci'):
                crea_file(nome_lista)
        case Actions.CANCELLA:
            os.system('cls')
            listFile()
            print()
            indice = input("Inserisci l'indice dell'elemento da cancellare(o esci per tornare indietro senza cancellare): ")
            if(indice != 'esci'):
                cancella(int(indice))
        case Actions.MODIFICA:
            os.system('cls')
            listFile()
            print()
            print("Modifica")
            input()
        case Actions.USCITA:
            os.system('cls')
            print("Programma terminato")
        case _:
            os.system('cls')
            print("Scelta non valida")
            input()




