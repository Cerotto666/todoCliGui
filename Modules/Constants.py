from pathlib import Path

"""
Classe che contiene i valori costanti utilizzati nel codice
"""
class Actions:
    USCITA = 0
    CREA = 1
    CANCELLA = 2
    MODIFICA = 3
    INPUT_NON_VALIDO = -1

    EDIT_AGGIUNGI = 1
    EDIT_MODIFICA = 2
    EDIT_CANCELLA = 3

class Windows_name:
    HOME = 1
    MODIFICA = 2
    VISUALIZZA = 3


directory = Path("./Files")