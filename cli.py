from Modules.MenuCli import *
import os

scelta = -1

while(scelta != Actions.USCITA):

    scelta = stampa_menu()

    match scelta:
        case Actions.CREA:
            crea_file()
        case Actions.CANCELLA:
            cancella_file()
        case Actions.MODIFICA:
            modifica_file()
        case Actions.USCITA:
            esci_programma()
        case _:
            default_case(scelta)





